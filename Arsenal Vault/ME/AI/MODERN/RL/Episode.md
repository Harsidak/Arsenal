---
tags:
  - reinforcement-learning
  - sutton-barto
  - rl-basics
aliases:
  - episode
  - episodes
  - Episodic Tasks
  - Continuous Tasks
---

# 🎬 Episodes, Steps, and Training Horizons

> [!NOTE] Foundations & Context
> In Reinforcement Learning, the flow of time and experience is structured into hierarchical units of interaction. Understanding the relationship between **Steps**, **Episodes**, and **Total Training Steps** is critical for designing agent behavior for both finite achievements and perpetual hardware control.

---

## 1. The Hierarchy of Experience

To build an intuitive grasp of how an AI learns, we must break down its experience into three nested dimensions: the **Step**, the **Episode**, and the **Total Training Horizon**.

```mermaid
graph TD
    subgraph Career ["🏋️ TOTAL TRAINING HORIZON (e.g., 1,000,000 Steps)"]
        direction TB
        E1["🥊 Episode 1<br>(100% to 0% Battery Run)"]
        E2["🥊 Episode 2<br>(Translation Task Run)"]
        E3["🥊 Episode 3<br>(Navigation Task Run)"]
        Dot["..."]
        
        subgraph Ep ["🎬 AN EPISODE (Single Complete Run)"]
            direction LR
            S1["⚡ Step 1<br>(Action A_0)"] --> S2["⚡ Step 2<br>(Action A_1)"]
            S2 --> S3["⚡ Step 3<br>(Action A_2)"]
            S3 --> ST["🏁 Terminal State (S_T)"]
        end
        
        Career -.-> E1
        Career -.-> Ep
        Career -.-> E2
        Career -.-> E3
        Career -.-> Dot
    end

    style Career fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#f8fafc
    style Ep fill:#1e293b,stroke:#10b981,stroke-width:2px,color:#f8fafc
    style S1 fill:#334155,stroke:#94a3b8,color:#f8fafc
    style S2 fill:#334155,stroke:#94a3b8,color:#f8fafc
    style S3 fill:#334155,stroke:#94a3b8,color:#f8fafc
    style ST fill:#f43f5e,stroke:#fda4af,color:#f8fafc
```

### 🥊 The Boxing Analogy
Imagine training to become a professional championship boxer:

| Dimension | 🥊 The Boxing Analogy | 👓 ONYX Smart Glasses (Battery Management) |
| :--- | :--- | :--- |
| **A Step** | **A single punch or dodge.** The immediate micro-action taken at a fraction of a second. | **Every 1 second**, ONYX checks current voltage and decides to either dim the screen, scale the processor, or keep full brightness. |
| **An Episode** | **One complete match.** It begins when the bell rings, lasts for several rounds of punches (steps), and terminates when the referee declares a winner or the timer runs out. | **A single continuous drain.** ONYX starts at 100% battery, executes power-scaling actions every second, and hits a **Terminal State ($S_T$)** when the battery hits 0% and the glasses shut off (e.g., 5,000 steps). |
| **Total Training** | **Your entire career.** Throwing millions of punches across hundreds of training fights until you master the optimal defense and counter-punches. | **1,000,000 cumulative steps.** ONYX drains the battery, logs the rewards, recharges, and restarts the environment back-to-back across ~200 episodes until it has executed 1M total actions. |

---

## 2. Episodic vs. Continuous Tasks

In Reinforcement Learning, environments are strictly classified into two categories based on their ending criteria:

### 1. Episodic Tasks (Has a Clear Finish Line)
Episodic tasks naturally end. They start in an initial state ($S_0$) and are guaranteed to hit a **Terminal State ($S_T$)** which resets the environment. 
*   **The Gaming Analogy**: In *Super Mario*, an episode starts at the beginning of Level 1-1. Mario runs, jumps, and gathers coins (steps). The episode terminates when he either touches the flagpole (success) or falls in a pit (failure). The screen resets, and a new episode begins.
*   **👓 ONYX Application (Billboard Translation)**: The user looks at a billboard and commands, *"ONYX, translate this text."* 
    1.  **State $S_0$**: Text detected on the camera feed.
    2.  **Action $A_0$**: Capture high-resolution crop.
    3.  **Action $A_1$**: Send to OCR and translation pipeline.
    4.  **Action $A_2$**: Project translated overlay onto AR waveguides.
    5.  **Terminal State $S_T$**: Translation projected successfully. The episode finishes, and the system sleeps, waiting for the next command.

### 2. Continuous Tasks (Infinite / Never-Ending)
Continuous tasks have no natural terminal state. The interaction loop goes on indefinitely unless forced to stop by external factors (like hardware failure or power cuts).
*   **The Physics Analogy**: Keeping an industrial active heating element stabilized, or maintaining high-voltage grid stability.
*   **👓 ONYX Application (Thermal Management)**: 
    *   ONYX must prevent smart glasses processors from overheating while keeping AR refresh rates fluid.
    *   The system constantly checks temperatures and balances clock cycles in a perpetual feedback loop. 
    *   There is no "finish line" to cooling; the agent must run continuously until the battery dies or the glasses are turned off.

---

## 3. Why RL Algorithms (PPO, TRPO) Care About Episodes

Modern policy optimization algorithms like **PPO (Proximal Policy Optimization)** and **TRPO (Trust Region Policy Optimization)** depend heavily on episodic horizons to execute weight updates:

### ⏳ The Credit Assignment Challenge
Suppose an AI agent is learning to play chess:
*   Moving your Knight on **Turn 3** might feel like a neutral move (immediate reward = 0).
*   However, that exact move opened up a tactical path that allowed you to capture the Queen on **Turn 28**, leading to a checkmate (final reward = +100).
*   If the agent updated its neural network weights after every single step, it would never learn the value of the Turn 3 move because there was no immediate feedback.

### 🔍 The Episodic Return Solution
To solve this, policy algorithms wait for a complete **Episode** (or a fixed trajectory window) to play out. Once the episode terminates, the algorithm calculates the **Discounted Return ($G_t$)** at each step:

$$G_t = \sum_{k=0}^{T-t-1} \gamma^k R_{t+k+1}$$

Where:
*   $R$ represents rewards collected at each step.
*   $\gamma$ (gamma) is the discount factor (typically $0.99$), representing how much the agent values immediate rewards over future ones.

By looking back from the terminal state, the agent can calculate the **Advantage** of every single action taken along the way. If the episode ended in a massive victory, the algorithm pushes the weights of *all* decisions taken in that episode (including the early Turn 3 move) to make them more likely to occur in future episodes.

---

## 4. The Training Loop Math

When you configure your training script with `total_timesteps = 1000000`, the environment behaves like an infinite loop of episodes:

```
Initialize S_0
Loop until total_steps reaches 1,000,000:
    Select Action A_t using Policy π(S_t)
    Step environment: S_t+1, Reward R_t, Is_Terminal
    Accumulate training step count + 1
    
    If Is_Terminal:
        Calculate returns and update Policy weights
        Reset Environment to S_0 (Start New Episode)
```

The mathematical summation of training simply runs as:

$$\text{Total Training Steps (1,000,000)} = \sum_{e=1}^{E} \text{Steps in Episode } e$$

If Episode 1 takes 5,000 steps, Episode 2 takes 3,000 steps, and Episode 3 takes 6,000 steps, the training agent will automatically cycle through roughly 200 consecutive episodes, constantly resetting the system, until it has collected exactly 1,000,000 steps of physical experience.

---

## 🔗 Related Notes
*   [[Reinforcement Learning]]
*   [[BOOK - REINFORCEMENT LEARNING (Sutton & Barto)]]
*   [[Arbitrary Control Rules]]
*   [[Markov Decision Process]]
*   [[Discount Rate]]
*   [[Markov Property]]
*   [[Value Function]]
*   [[Bellman Equation]]
