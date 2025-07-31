# 🔁 RL² — Recurrent Meta-Reinforcement Learning Agent

This branch contains a clean PyTorch implementation of **RL² (Reinforcement Learning Squared)** — a memory-based meta-reinforcement learning algorithm that learns to adapt to new tasks using a recurrent policy.

---

## 📚 What is RL²?

RL² is a meta-learning algorithm introduced in the paper:

> **"RL²: Fast Reinforcement Learning via Slow Reinforcement Learning"**

> *Yan Duan et al., 2016* — [arXiv:1611.02779](https://arxiv.org/abs/1611.02779)

It trains an **RNN-based policy** that can adapt to different tasks by processing entire trajectories of `(state, action, reward)` tuples.  
This allows the agent to **learn how to learn**, by encoding experience into its hidden state — no explicit task embedding, no inner-loop gradient steps.

---

## 🧠 Why Use RL²?

- **Online adaptation**: Handles changing dynamics or goals mid-episode.
  
- **Recurrent memory**: Learns task-specific behavior via hidden states.
  
- **No gradient-based inner loop**: Simpler and more stable than MAML-like methods.
  
- Great for **meta-environments** with multiple task distributions.

---

## 🛠️ What's Implemented Here

- ✅ **Recurrent Policy** using separate LSTM layers for actor and critic.
- ✅ **Feature extractor** for `(state, prev_action, prev_reward)` tuples.
- ✅ **Tanh-squashed Gaussian policy** with log-prob correction.
- ✅ **Value function head** for critic with shared input processing.
- ✅ **Meta episode runner** for looping over tasks and episodes.
- ✅ **Meta replay buffer** (episode-level) with support for:
  - Padding
  - Masking
  - Variable-length sequences
- ✅ **Hidden state initialization/reset per episode**
- ✅ **Training script** with policy loss, value loss, and reward logging.
- ✅ **TensorBoard integration**
- ✅ **Notebook** with visualizations and explanations

---

This branch logs the following metrics to TensorBoard:

policy_loss: Actor's objective

<img width="800" height="500" alt="Figure_1" src="https://github.com/user-attachments/assets/2df84e24-c55a-4582-bdd5-c6ecdf82c3d6" />


value_loss: Critic MSE

<img width="800" height="500" alt="Figure_2" src="https://github.com/user-attachments/assets/97bc8745-b417-44da-b6d4-a89c4c98055f" />

### 🧠 What You'll Learn by Studying This

Why hidden states are central to online task adaptation.

How meta-level runners and buffers differ from standard RL.

How to handle sequence padding, masking, and variable episode lengths.

The simplicity and power of recurrent adaptation in multi-task environments.

### 📎 Citation & Credit

Implementation inspired by:

**RL² (Duan et al. 2016)**

**Meta-RL benchmarks**
