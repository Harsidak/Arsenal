# 📘 Book - Reinforcement Learning: An Introduction

> [!NOTE] Authors
> **Richard S. Sutton and Andrew G. Barto** (The seminal textbook on RL)
> **Links**: [[Reinforcement Learning]] | [[AI]]

---

## 🧠 Simpler Breakdown of RL Foundations

### 1. The Core Agent-Environment Loop
*   **The Simple Idea**: RL is the study of how an active agent learns to make optimal decisions in a dynamic world through trial and error.
*   **Key Components**:
    *   **Agent**: The brain/decision-maker.
    *   **Environment**: The world the agent interacts with.
    *   **State ($S_t$)**: The current setup of the world.
    *   **Action ($A_t$)**: What the agent decides to do.
    *   **Reward ($R_t$)**: The score (+ or -) the agent gets for its action.
*   **Why it matters**: It is the closest mathematical model we have to how biological systems learn (learning through pain and pleasure).

### 2. Markov Decision Processes (MDPs)
*   **The Simple Idea**: The formal framework for describing an RL environment.
*   **The Markov Property**: *"The future is independent of the past given the present."* (You only need the current state $S_t$ to make an optimal decision; you don't need the entire history).
*   **Why it matters**: It simplifies massive math equations. Instead of tracking a robot's entire lifetime of movements, we only need to look at its current position, velocity, and orientation to calculate its next action.

### 3. The Exploration vs. Exploitation Dilemma
*   **The Simple Idea**: 
    *   **Exploitation**: Choosing the action you *know* gives a good reward (e.g., going to your favorite restaurant).
    *   **Exploration**: Trying something new that might be terrible or might be the best thing ever (e.g., trying a random new food truck).
*   **Why it matters**: If an agent only exploits, it gets stuck in sub-optimal behaviors. If it only explores, it never gathers high rewards. Methods like **$\epsilon$-greedy** force the agent to explore a small percentage of the time (e.g., 10%) so it keeps discovering better paths.

### 4. Value Functions & Bellman Equations
*   **The Simple Idea**: How do you measure the value of a state? It's not just the immediate reward, but the sum of all future rewards you expect to get from that point onward, discounted by time ($\gamma$).
*   **The Bellman Equation**: Breaks the value of a state down into the *immediate reward* plus the discounted *value of the next state*:
    $$V(s) = R(s) + \gamma \sum_{s'} P(s' | s, a) V(s')$$
*   **Why it matters**: This equation is the mathematical engine of RL. It allows agents to calculate long-term value recursively, enabling them to evaluate the consequence of their actions far into the future.

### 5. Policy Optimization & Policy Gradients
*   **The Simple Idea**: Rather than estimating how good states are (value-based), we can directly train the model's action strategy (policy $\pi$) using gradient ascent to maximize expected rewards.
*   **Why it matters**: This is the foundation of modern Large Language Model alignment. Techniques like **RLHF** and **PPO / GRPO** utilize policy gradients to adjust model weights so they generate safe, accurate, and highly reasoning-rich text responses.

---

## 🎯 The Big Picture
*   **MDPs** [[Markov Decision Process]] define the mathematical sandbox.
*   **Agent-Environment Boundary** [[Arbitrary Control Rules]] defines the limit of arbitrary control.
*   **Episodic vs. Continuous Tasks** [[Episode]] outlines the structuring of time and returns.
*   **Discount Factor (Gamma)** [[Discount Rate]] bounds future rewards and scales agent impatience.
*   **Markov Property (Memorylessness)** [[Markov Property]] guarantees the present is all that matters.
*   **Value Functions (V & Q)** [[Value Function]] act as the agent's long-term future reward estimators.
*   **Bellman Equations** [[Bellman Equation]] establish recursive value profiles across temporal steps.
*   **Exploration/Exploitation** balances finding new strategies versus using known ones.
*   **Policy Gradients** adjust the neural network to produce high-value behavior.
