"""
ANN for Fashion-MNIST — Research-Grade Implementation
Lt. Banwait / BaN-WaiT Arsenal
"""

import os
import random
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchinfo import summary


# ══════════════════════════════════════════════════════════════════════════════
# 0. REPRODUCIBILITY
# ══════════════════════════════════════════════════════════════════════════════

def seed_everything(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark     = False

seed_everything(42)


# ══════════════════════════════════════════════════════════════════════════════
# 1. CONFIG — single source of truth for every hyperparameter
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class ANNConfig:
    # Data
    data_dir    : str        = "./data"
    num_classes : int        = 10
    input_dim   : int        = 784          # 28×28 flattened

    # Architecture — change these to experiment with depth/width
    hidden_dims : List[int]  = field(default_factory=lambda: [512, 256, 128])
    dropout_p   : float      = 0.3
    use_batchnorm: bool      = True
    activation  : str        = "gelu"       # "relu" | "gelu" | "silu" | "leaky_relu"

    # Training
    batch_size  : int        = 64
    epochs      : int        = 20
    lr          : float      = 1e-3
    weight_decay: float      = 1e-4
    clip_grad   : float      = 1.0

    # System
    device      : str        = field(
        default_factory=lambda: "cuda" if torch.cuda.is_available() else "cpu"
    )
    num_workers : int        = 2

    # Fashion-MNIST class names for readable output
    class_names : List[str]  = field(default_factory=lambda: [
        "T-shirt", "Trouser", "Pullover", "Dress",   "Coat",
        "Sandal",  "Shirt",   "Sneaker",  "Bag",     "Ankle boot"
    ])


# ══════════════════════════════════════════════════════════════════════════════
# 2. DATA PIPELINE
# ══════════════════════════════════════════════════════════════════════════════

def get_dataloaders(cfg: ANNConfig) -> Tuple[DataLoader, DataLoader]:
    """
    Downloads Fashion-MNIST automatically.
    Applies normalization using dataset mean=0.2860, std=0.3530.
    """
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.2860,), std=(0.3530,)),  # Fashion-MNIST stats
        transforms.Lambda(lambda x: x.view(-1))               # flatten 28×28 → 784
    ])

    train_dataset = datasets.FashionMNIST(
        root=cfg.data_dir, train=True,  download=True, transform=transform
    )
    test_dataset = datasets.FashionMNIST(
        root=cfg.data_dir, train=False, download=True, transform=transform
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size  = cfg.batch_size,
        shuffle     = True,
        num_workers = cfg.num_workers,
        pin_memory  = cfg.device == "cuda"     # faster GPU transfer
    )
    test_loader = DataLoader(
        test_dataset,
        batch_size  = cfg.batch_size,
        shuffle     = False,
        num_workers = cfg.num_workers,
        pin_memory  = cfg.device == "cuda"
    )

    print(f"Train samples : {len(train_dataset):,}")
    print(f"Test  samples : {len(test_dataset):,}")
    return train_loader, test_loader


# ══════════════════════════════════════════════════════════════════════════════
# 3. MODEL — the robust ANN class
# ══════════════════════════════════════════════════════════════════════════════

class FashionANN(nn.Module):
    """
    Configurable ANN for Fashion-MNIST.

    Architecture per hidden layer:
        Linear → [BatchNorm] → Activation → Dropout

    Final layer:
        Linear(last_hidden → num_classes)
        NO activation — CrossEntropyLoss handles softmax internally.

    Args:
        cfg: ANNConfig dataclass controlling depth, width, and regularization.
    """

    # Map string names to nn activation classes
    _ACTIVATIONS: Dict[str, type] = {
        "relu"       : nn.ReLU,
        "gelu"       : nn.GELU,
        "silu"       : nn.SiLU,
        "leaky_relu" : nn.LeakyReLU,
    }

    def __init__(self, cfg: ANNConfig) -> None:
        super().__init__()

        if cfg.activation not in self._ACTIVATIONS:
            raise ValueError(
                f"Unknown activation '{cfg.activation}'. "
                f"Choose from {list(self._ACTIVATIONS.keys())}"
            )

        self.cfg   = cfg
        self.net   = self._build_network()
        self._init_weights()

    def _build_network(self) -> nn.Sequential:
        """
        Dynamically builds layers from cfg.hidden_dims.
        Changing hidden_dims in config rewires the entire network — zero code change.
        """
        layers     : List[nn.Module] = []
        in_features: int             = self.cfg.input_dim
        ActClass                     = self._ACTIVATIONS[self.cfg.activation]

        for hidden_dim in self.cfg.hidden_dims:
            # ── Linear ───────────────────────────────────────────────────────
            layers.append(nn.Linear(in_features, hidden_dim))

            # ── BatchNorm (before activation — pre-activation style) ─────────
            if self.cfg.use_batchnorm:
                layers.append(nn.BatchNorm1d(hidden_dim))

            # ── Activation ───────────────────────────────────────────────────
            layers.append(ActClass())

            # ── Dropout ──────────────────────────────────────────────────────
            layers.append(nn.Dropout(p=self.cfg.dropout_p))

            in_features = hidden_dim   # next layer's input = this layer's output

        # Output layer — raw logits, no activation
        layers.append(nn.Linear(in_features, self.cfg.num_classes))

        return nn.Sequential(*layers)

    def _init_weights(self) -> None:
        """
        Kaiming uniform init for linear layers (correct for ReLU-family).
        Zeros for biases. BatchNorm init left at PyTorch default (weight=1, bias=0).
        """
        for module in self.modules():
            if isinstance(module, nn.Linear):
                nn.init.kaiming_uniform_(module.weight, nonlinearity="relu")
                if module.bias is not None:
                    nn.init.zeros_(module.bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: shape (batch_size, 784) — pre-flattened input
        Returns:
            logits: shape (batch_size, 10) — raw scores, no softmax
        """
        return self.net(x)

    def predict(self, x: torch.Tensor) -> torch.Tensor:
        """Inference-mode forward — returns class indices, not logits."""
        self.eval()
        with torch.no_grad():
            logits = self.forward(x)
            return logits.argmax(dim=1)

    def predict_proba(self, x: torch.Tensor) -> torch.Tensor:
        """Returns softmax probabilities for all 10 classes."""
        self.eval()
        with torch.no_grad():
            logits = self.forward(x)
            return torch.softmax(logits, dim=1)


# ══════════════════════════════════════════════════════════════════════════════
# 4. TRAINER CLASS
# ══════════════════════════════════════════════════════════════════════════════

class Trainer:
    def __init__(
        self,
        model       : FashionANN,
        train_loader: DataLoader,
        test_loader : DataLoader,
        cfg         : ANNConfig,
    ) -> None:
        self.model        = model.to(cfg.device)
        self.train_loader = train_loader
        self.test_loader  = test_loader
        self.cfg          = cfg

        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = torch.optim.AdamW(
            self.model.parameters(),
            lr           = cfg.lr,
            weight_decay = cfg.weight_decay
        )
        # LR scheduler — reduces LR when val loss plateaus
        self.scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            self.optimizer, mode="min", patience=3, factor=0.5, verbose=True
        )

        self.history: Dict[str, List[float]] = {
            "train_loss": [], "val_loss": [], "val_acc": []
        }
        self.best_val_loss  : float               = float("inf")
        self.best_model_wts : Optional[dict]      = None

    # ── Single training epoch ────────────────────────────────────────────────
    def _train_epoch(self) -> float:
        self.model.train()
        total_loss = 0.0

        for x_batch, y_batch in self.train_loader:
            x_batch = x_batch.to(self.cfg.device)
            y_batch = y_batch.to(self.cfg.device)

            self.optimizer.zero_grad()
            logits = self.model(x_batch)
            loss   = self.criterion(logits, y_batch)
            loss.backward()

            # Gradient clipping — prevents exploding gradients
            nn.utils.clip_grad_norm_(self.model.parameters(), self.cfg.clip_grad)

            self.optimizer.step()
            total_loss += loss.item()

        return total_loss / len(self.train_loader)

    # ── Evaluation ───────────────────────────────────────────────────────────
    @torch.no_grad()
    def _evaluate(self) -> Tuple[float, float]:
        self.model.eval()
        total_loss = 0.0
        correct    = 0
        total      = 0

        for x_batch, y_batch in self.test_loader:
            x_batch = x_batch.to(self.cfg.device)
            y_batch = y_batch.to(self.cfg.device)

            logits  = self.model(x_batch)
            loss    = self.criterion(logits, y_batch)
            total_loss += loss.item()

            preds   = logits.argmax(dim=1)
            correct += (preds == y_batch).sum().item()
            total   += y_batch.size(0)

        val_loss = total_loss / len(self.test_loader)
        val_acc  = correct / total
        return val_loss, val_acc

    # ── Per-class accuracy report ─────────────────────────────────────────────
    @torch.no_grad()
    def class_report(self) -> None:
        self.model.eval()
        class_correct = torch.zeros(self.cfg.num_classes)
        class_total   = torch.zeros(self.cfg.num_classes)

        for x_batch, y_batch in self.test_loader:
            x_batch = x_batch.to(self.cfg.device)
            y_batch = y_batch.to(self.cfg.device)
            preds   = self.model(x_batch).argmax(dim=1)

            for c in range(self.cfg.num_classes):
                mask           = (y_batch == c)
                class_correct[c] += (preds[mask] == c).sum().item()
                class_total[c]   += mask.sum().item()

        print("\n── Per-class accuracy ──────────────────────")
        for i, name in enumerate(self.cfg.class_names):
            acc = 100.0 * class_correct[i] / class_total[i]
            bar = "█" * int(acc // 5)
            print(f"{name:<12} {acc:5.1f}%  {bar}")

    # ── Main training loop ────────────────────────────────────────────────────
    def fit(self) -> None:
        print(f"\nTraining on : {self.cfg.device.upper()}")
        print(f"Architecture: {self.cfg.hidden_dims} → {self.cfg.num_classes}")
        print(f"Activation  : {self.cfg.activation.upper()}")
        print("─" * 60)

        for epoch in range(1, self.cfg.epochs + 1):
            train_loss          = self._train_epoch()
            val_loss, val_acc   = self._evaluate()

            self.history["train_loss"].append(train_loss)
            self.history["val_loss"].append(val_loss)
            self.history["val_acc"].append(val_acc)

            # Checkpoint best model
            if val_loss < self.best_val_loss:
                self.best_val_loss  = val_loss
                self.best_model_wts = {
                    k: v.cpu().clone() for k, v in self.model.state_dict().items()
                }

            # Step scheduler on val loss
            self.scheduler.step(val_loss)

            if epoch % 2 == 0 or epoch == 1:
                print(
                    f"Epoch {epoch:03d}/{self.cfg.epochs} | "
                    f"Train Loss: {train_loss:.4f} | "
                    f"Val Loss: {val_loss:.4f} | "
                    f"Val Acc: {val_acc*100:.2f}%"
                )

        # Restore best weights
        if self.best_model_wts:
            self.model.load_state_dict(self.best_model_wts)
        print("\nTraining complete. Best weights restored.")

    def save(self, path: str = "fashion_ann_best.pt") -> None:
        torch.save({
            "model_state_dict"  : self.model.state_dict(),
            "optimizer_state"   : self.optimizer.state_dict(),
            "config"            : self.cfg,
            "history"           : self.history,
            "best_val_loss"     : self.best_val_loss,
        }, path)
        print(f"Checkpoint saved → {path}")

    @classmethod
    def load(cls, path: str, cfg: ANNConfig) -> "FashionANN":
        checkpoint = torch.load(path, map_location=cfg.device)
        model      = FashionANN(checkpoint["config"])
        model.load_state_dict(checkpoint["model_state_dict"])
        print(f"Model loaded from {path}")
        return model


# ══════════════════════════════════════════════════════════════════════════════
# 5. EXECUTION
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    cfg = ANNConfig()
    print(f"Device: {cfg.device}")

    # Data
    train_loader, test_loader = get_dataloaders(cfg)

    # Model
    model = FashionANN(cfg)
    summary(model, input_size=(cfg.batch_size, cfg.input_dim))

    # Train
    trainer = Trainer(model, train_loader, test_loader, cfg)
    trainer.fit()

    # Per-class breakdown
    trainer.class_report()

    # Save
    trainer.save("fashion_ann_best.pt")
