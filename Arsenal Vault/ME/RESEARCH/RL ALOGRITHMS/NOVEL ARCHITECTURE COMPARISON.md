---
tags:
  - research
  - architecture
  - low-latency
  - co-design
  - wearables
  - rl-theory
aliases:
  - novel architectures
  - wearable AI systems
  - hardware-software co-design
  - ONYX Architecture
  - RL baselines
  - PPO vs GRPO
---

# 🌌 Novel Computing & RL Architectures: Evolution & Comparison

> [!NOTE] Research Mission & Vision Statement
> *"To advance the frontier of next-generation wearable and algorithmic intelligence, we actively pioneer systems that bridge the gap between human experience and digital perception. Our current research is centered on three core pillars: **Multimodal Perception**, **Low-Latency Model Optimization**, and **Hardware-Software Co-Design** for embedded wearables. The goal is absolute: to deliver useful, reliable, and ultra-low-latency AI that integrates so structurally into daily human workflows that the technology itself becomes practically invisible."*

---

## 1. The Wearable Systems Paradigm (BaN-WaiT / Project ONYX)

Designing artificial intelligence for standalone, battery-powered wearable devices requires balancing continuous high-fidelity sensory processing against physical hardware bounds: thermal dissipation, battery depletion, mechanical space limits, and RAM ceilings.

### 🔌 Hardware-Software Co-Design (The GPIO Breakthrough)
Off-the-shelf accessories often assume exclusive access to physical connectors, resulting in mechanical-electrical deadlocks on tiny wearable boards.
*   **The Contention**: The high-speed AR display module occupies the top GPIO pin header, physically blocking access to the power/control pins required by the active cooling fan.
*   **The Co-Design Solution**: We inverted the board layout and utilized the soldered through-hole terminations on the **underside of the board**. By attaching and mechanically stabilizing the fan connector to the bottom-side solder points, we unlocked simultaneous electrical access to the same power rails. 
*   This physical multiplexing allows the software's active cooling daemon to operate concurrently with the display driver, preventing processor thermal lockouts under high inference load.

### 🎙️ Multimodal Perception & Signal Conditioning
Wearable interaction demands continuous, low-overhead sensory capture. In the ONYX architecture, we resolve this through programmatic high-level abstractions:
*   **Picamera2 API Integration**: Bypassing CLI wrappers (`libcamera-still`) to utilize direct Userspace Python memory mapping, ensuring instantaneous capture verification without PATH dependencies.
*   **Decoupled Audio Pipelines**: Capturing audio at the USB microphone's native rate (44.1 kHz) to preserve signal stability and prevent driver overflows, followed by post-capture downsampling to 16 kHz to satisfy the input requirements of **Whisper-Tiny** command-parsing.

---

## 2. Mathematical Armory: Objective Function Evolution

The following sections detail the mathematical baseline evolution of objective functions, tracing the development path from traditional baseline PPO to your custom, memory-optimized Kaggle hybrid.

```
       [ 1. PPO (Baseline) ] ────► Symmetric clipping, high-VRAM dual-model dependency (Policy + Critic)
                 │
                 ▼
       [ 2. GRPO (VRAM Saver) ] ──► Deletes Critic model, introduces Group-Relative Advantage & KL band
                 │
                 ▼
       [ 3. DAPO (Length Normal) ] ► Introduces Global Length Normalizer & Asymmetric bounds
                 │
                 ▼
       [ 4. BAPO (Dynamic Suspen) ] ► Discards rigid limits for Dynamic Bounds preserving entropy
                 │
                 ▼
  [ 5. Custom Kaggle Architecture ] ► Hybrid: DAPO Global Normalizer + BAPO Dynamic Bounds
                                      Data Filter active, KL reference model stripped for VRAM survival
```

---

### A. PPO (Proximal Policy Optimization)
*The Baseline Engine*

PPO introduced a "pessimistic governor" using a symmetric concrete wall to prevent a policy from executing destabilizingly large updates that could degrade neural network weights.

> [!IMPORTANT] PPO Clip Objective Function
> $$L^{CLIP}(\theta) = \hat{\mathbb{E}}_{t} \left[ \min \left( r_t(\theta)\hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t \right) \right]$$

#### Equation Parameters:
*   **$r_t(\theta)$**: The probability ratio of the new policy to the old policy: $\frac{\pi_\theta(a_t \mid s_t)}{\pi_{\theta_{\text{old}}}(a_t \mid s_t)}$.
*   **$\hat{A}_t$**: The Advantage estimate, indicating if the action chosen performed better than the baseline average.
*   **$\text{clip}(\dots)$**: Restricts the ratio $r_t(\theta)$ to a strict interval $[1-\epsilon, 1+\epsilon]$ (typically $\epsilon = 0.2$), removing incentives for the policy to push updates outside the trust region.

---

### B. GRPO (Group Relative Policy Optimization)
*The VRAM Saver*

Pioneered by DeepSeek, GRPO completely deletes the massive Critic/Value Model from the active GPU footprint, saving massive amounts of VRAM. Instead, it generates a group of $G$ answers for a single prompt, averages their scores to establish the baseline dynamically, and reintroduces a KL Divergence penalty to prevent policy degradation.

> [!IMPORTANT] GRPO Objective Function
> $$\mathcal{J}_{GRPO}(\theta) = \mathbb{E} \left[ \frac{1}{G} \sum_{i=1}^G \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} \left\{ \min \left( r_{i,t}(\theta) \hat{A}_{i,t}, \text{clip}(r_{i,t}(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_{i,t} \right) - \beta \mathbb{D}_{KL} [\pi_\theta \mid\mid \pi_{\text{ref}}] \right\} \right]$$

#### The Group-Relative Advantage ($\hat{A}_{i,t}$):
Unlike PPO, which queries a Critic model for values, GRPO evaluates advantages relatively within the generated cohort:

$$\hat{A}_{i,t} = \frac{R_i - \text{mean}(\mathcal{G})}{\text{std}(\mathcal{G})}$$

*   **$\beta \mathbb{D}_{KL} [\pi_\theta \mid\mid \pi_{\text{ref}}]$**: A Kullback-Leibler divergence penalty that acts as a rubber band, pulling the active policy back toward the reference model to prevent the agent from exploiting flaws in the reward system (reward hacking).

---

### C. DAPO (Direct Alignment for Policy Optimization)
*The Length-Exploitation Turbocharger*

DAPO builds on the GRPO baseline but introduces a global word-count normalizer to stop the AI from cheating with bloated, verbose answers (a common exploit where agents write long texts to inflate reward scores). It utilizes asymmetric speed limits and filters out low-value data from the calculations.

> [!IMPORTANT] DAPO Objective Function
> $$\mathcal{J}_{DAPO}(\theta) = \mathbb{E} \left[ \frac{1}{\sum_{i=1}^G |o_i|} \sum_{i=1}^G \sum_{t=1}^{|o_i|} \min \left( r_{i,t}(\theta)\hat{A}_{i,t}, \text{clip}(r_{i,t}(\theta), 1 - \epsilon_{low}, 1 + \epsilon_{high})\hat{A}_{i,t} \right) \right]$$

#### Key Features:
*   **Global Length Normalization ($\frac{1}{\sum |o_i|}$)**: Scores are normalized by the cumulative length of all generated outputs in the cohort, penalizing verbosity and encouraging concise, high-density reasoning.
*   **Asymmetric Clipping Bounds ($1-\epsilon_{low}, 1+\epsilon_{high}$)**: Recognizes that policy changes for negative outcomes should have different step limits than policy shifts for positive advantages.
*   **The Goldilocks Data Constraint**:
    $$s.t.\ \ 0 < |\{o_i \mid \text{is\_equivalent}(a, o_i)\}| < G$$
    This active filter discards groups where *all* or *none* of the generated answers are equivalent to the target answer $a$. If all answers are correct or all are wrong, the gradient update is flat; discarding them preserves valuable compute.

---

### D. BAPO (Balanced Policy Optimization)
*The Dynamic Suspension*

BAPO rejects rigid, hard-coded clipping limits. It dynamically recalculates the clipping boundaries on the fly during training to ensure a perfect equilibrium between positive policy updates and negative penalizations, preventing the policy's exploratory creativity (entropy) from collapsing.

> [!IMPORTANT] BAPO Objective Function
> $$\mathcal{J}_{BAPO}(\theta) = \mathbb{E} \left[ \frac{1}{G} \sum_{i=1}^G \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} \min \left( r_{i,t}(\theta) \hat{A}_{i,t}, \text{clip}(r_{i,t}(\theta), c_{low}^{*}, c_{high}^{*}) \hat{A}_{i,t} \right) \right]$$

#### The Dynamic Balancing Threshold:
The clipping bounds $c_{low}^{*}$ and $c_{high}^{*}$ are adjusted dynamically on each batch to satisfy the following reward-to-penalty ratio:

$$\frac{\left| \sum_{A_t > 0} [\min(r_t A_t, \text{clip}(r_t, 0, c_{high}^{*}) A_t)] \right|}{\left| \sum_{A_t < 0} [\min(r_t A_t, \text{clip}(r_t, c_{low}^{*}, c_{high}^{*}) A_t)] \right|} \ge \rho_0$$

This guarantees that the policy updates driven by positive reinforcement are structurally balanced against negative advantage constraints, preventing the gradient from being dominated by extreme values.

---

### E. The Custom Kaggle Architecture
*The VRAM-Optimized Hybrid Frankenstein Engine*

Designed to survive the strict **36GB VRAM memory ceiling** and **12-hour compute limits** of single-GPU Kaggle environments, this hybrid fuses DAPO's global length normalization and active data filters with BAPO's dynamic bounds. 

Crucially, **the KL Reference model is completely stripped out**. Loading a second, static reference model in memory consumes vast VRAM; by removing the KL model and enforcing dynamic bounds and constraints, the policy maintains stability without memory overhead.

> [!IMPORTANT] Custom Kaggle Hybrid Objective Function
> $$\mathcal{J}_{custom}(\theta) = \mathbb{E} \left[ \frac{1}{\sum_{i=1}^G |o_i|} \sum_{i=1}^G \sum_{t=1}^{|o_i|} \min \left( r_{i,t}(\theta)\hat{A}_{i,t}, \text{clip}(r_{i,t}(\theta), c_{low}^{*}, c_{high}^{*})\hat{A}_{i,t} \right) \right] - \mathcal{L}_{KL\_Proxy}$$

#### Active Runtime Constraints:
1.  **Data Ingestion Filter**:
    $$s.t.\ \ 0 < |\{o_i \mid \text{is\_equivalent}(a, o_i)\}| < G$$
    Keeps the pipeline highly efficient by instantly filtering out non-informative groups prior to loss computation.
2.  **Dynamic Bounds Regulation**:
    The boundaries $c_{low}^{*}$ and $c_{high}^{*}$ dynamically adjust on each training iteration to satisfy a ratio threshold of:
    $$\rho_0 \ge 0.4$$
    This maintains entropy and convergence stability without requiring a secondary KL reference model.

#### ⚖️ Zero-VRAM Weight-Space KL Proxy (Frobenius Constrained Drift)

To achieve a zero-VRAM footprint, we abandon probability-space KL divergence entirely. Instead, we constrain the model by strictly limiting the physical distance the active weights can drift from their initial SFT state. 

Because neural network mappings are locally continuous, bounding the perturbation in weight space ($\Delta W$) effectively bounds the drift in the functional output space. We define our KL proxy as the Squared Frobenius Norm of the difference between the active LoRA weights and the frozen SFT LoRA snapshot:

$$\mathcal{L}_{KL\_Proxy} = \beta \sum_{l \in \text{LoRA}} || W_{\theta}^{(l)} - W_{ref}^{(l)} ||_F^2$$

##### Parameter Specification:
*   **$W_{\theta}^{(l)}$**: Represents the active parameters of the $l$-th LoRA matrix (either $A$ or $B$).
*   **$W_{ref}^{(l)}$**: Represents the exact immutable snapshot of that matrix taken at $t=0$.
*   **$\beta$**: The tension coefficient (the "rubber band" scalar).
*   **$|| \cdot ||_F^2$**: The squared Frobenius norm, which evaluates to the sum of the squared differences of all elements in the matrix.

#### 🔧 The Implementation Mechanics

To implement this without incurring the VRAM cost of a reference model, we utilize the specific structural properties of Low-Rank Adaptation (LoRA):

1. **The Immutable Snapshot ($t=0$)**:
   At initialization, before the optimizer takes a single step, we iterate through the model's parameters. We detach and clone the active `lora_A` and `lora_B` matrices, storing them in a disconnected dictionary. Because LoRA matrices are exponentially smaller than the base model (typically $\sim$50MB total), this snapshot costs statistically zero VRAM.
2. **The Forward Pass Measurement**:
   During `compute_loss`, we loop through the active LoRA parameters. For each matrix, we calculate the Euclidean distance from its corresponding snapshot:
   $$\Delta W = \sum (W_{\theta} - W_{ref})^2$$
3. **The Penalty Injection**:
   We sum these squared deltas across all trainable matrices, multiply by our $\beta$ scalar (e.g., $0.04$), and add it directly to the policy loss.

---

## 🔗 Related Notes
*   [[Problems in BaN-WaiT]]
*   [[Reinforcement Learning]]
*   [[Markov Property]]
*   [[Markov Decision Process]]
*   [[Arbitrary Control Rules]]
*   [[Value Function]]
*   [[Bellman Equation]]
