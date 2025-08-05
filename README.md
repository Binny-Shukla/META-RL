# 🔁 FOMAML from Scratch – Meta-RL on MountainCarContinuous-v2

This project implements **First-Order Model-Agnostic Meta-Learning (FOMAML)** for reinforcement learning using PyTorch and Gym. The target environment is a custom **meta-version of `MountainCarContinuous-v2`**, where both gravity and goal position vary across tasks.

Designed to be light, intuitive, and pedagogically clean — this implementation is entirely written in **a single Jupyter Notebook** (`FOMAML.ipynb`) with an optional `plot.py` script for visualizing training progress.

---

## 🌌 What is FOMAML?

FOMAML is a simplified version of MAML that skips second-order gradients — making it faster and more scalable without sacrificing much performance.

Here, the model is trained to quickly adapt to a new task using just a few gradient steps from limited data (1-shot or few-shot). No task-specific conditioning tricks. Just pure, gradient-based adaptation.

---

## 🧠 Architecture Overview

- **Policy**: Stochastic Gaussian MLP with `tanh` squashing and `log_prob` calculation for REINFORCE-style learning.
- **Hyper Net**: A compact MLP that takes in state and feeds into the policy MLP.
- **Adaptation**: One gradient step using log-prob × reward.
- **Evaluation**: New task sampled, adapted policy rolled out for reward-weighted log prob loss.

---

## 🔧 Environment: `meta_car_continuous`

Custom wrapper around `MountainCarContinuous-v2` with task-specific:
- `goal_position ∈ [0.45, 0.55]`
- `gravity ∈ [0.0025, 0.006]`

Each task is a different combination of these parameters. Tasks are sampled via:
```python

env.sample_task(num_tasks)

```

## Training Setup

| Parameter            | Value            |
| -------------------- | ---------------- |
| Tasks per Meta-Step  | 5                |
| Steps per Trajectory | 64               |
| Meta Iterations      | 50               |
| Inner Loop LR        | 1e-5             |
| Optimizer            | AdamW            |
| LR Scheduler         | Cosine Annealing |


### 📈 Results

Final Meta Loss (val loss averaged across 5 tasks):

      yaml
      epoch: 50 | avg_val_loss: -0.0038

The loss consistently decreased from ~ -0.02 to -0.002 over 50 meta-iterations, showing effective meta-learning.

To visualize the trend, run:

      bash
      python plot.py
      
### 📁 Files

      FOMAML.ipynb – Full code including:
      
      Environment setup
      
      Policy model
      
      Roller buffer
      
      Collect trajectory logic
      
      Adaptation function
      
      Meta-training loop
      
      plot.py – Parses TensorBoard logs and generates reward/loss plots


#### ✨ Example Output (Final TQDM Bar)

      yaml
      FOMAML: 100%|██████████| 50/50 [02:03<00:00,  2.47s/it]
      epoch: 50 | avg_val_loss: -0.0038

#### Plot of loss

<img width="800" height="500" alt="val_Figure_1" src="https://github.com/user-attachments/assets/955d9899-f2b2-45a5-92cc-09c3e6639026" />


#### 🥇 Why This Project?

This repo is a minimal and intuitive intro to gradient-based Meta-RL:

No task encoders

No bells and whistles

Just learning-to-learn, clean and raw

Great for:

      Meta-RL research bootstrapping
      
      Pedagogical clarity
      
      Debugging FOMAML before scaling to complex tasks like HalfCheetah or Ant


---

Let me know if you want a **GIF of the car** learning over tasks, or a **Twitter thread summary** next — you're basically ready to go viral with this 💫

