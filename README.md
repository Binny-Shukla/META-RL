# 🧭 Meta-RL Research Repository

Welcome to the Meta-RL Research Repository — a focused, hands-on exploration of the algorithms that teach agents how to **adapt, learn, and evolve** across tasks. This repository is built to understand the foundations, dynamics, and nuances of **Meta-Reinforcement Learning** (Meta-RL), with full-code implementations from scratch in PyTorch.

---

## 🌱 What This Repository Contains

This repo is structured around three key categories of Meta-RL:

1. **Gradient-Based Meta-RL**  
   - Algorithms like MAML, Reptile, Meta-SGD that adapt by inner-loop gradient updates.

2. **Contextual & Memory-Based Meta-RL**  
   - Algorithms like R² and PEARL that use memory or latent inference for fast adaptation.

3. **Population-Based Meta-RL**  
   - Evolution-inspired agents that evolve over distributions of tasks.

Each branch of this repo explores one algorithm deeply, including:
- Custom PyTorch implementations.
- Clean Jupyter notebooks for visualizing the training dynamics.
- Meta episode runners and meta replay buffers.
- Detailed README files to explain how and why things work.

---

## 🧩 Why This Repository Exists

Modern reinforcement learning often overfits to static tasks. Meta-RL teaches us **how agents can generalize** across multiple tasks and environments.  
Through building these algorithms from scratch, we aim to deeply understand:
- The role of **hidden states and recurrence** in adaptation.
- The structure of **task distributions**.
- The implementation of **meta-learning runners** and buffers.
- How to properly use **masking, padding**, and **sequence-aware architectures**.

This repo is **not a library**, but a **research playground**. Every implementation here is:
- From scratch.
- Debuggable and educational.
- Designed to be extended, modified, and studied.

## 🌟 How to Use This Repo

- Clone the repo.
- Checkout any specific algorithm branch (e.g. `r2`, `pearl`, `maml`).
- Read the local README.
- Run the Jupyter notebook or training script.
- Modify, visualize, and learn.

---

## 🧭 Roadmap

- [x] ✅ R² (Recurrent Meta-RL Agent)
- [ ] ⏳ PEARL (Latent Variable Conditioning)
- [x] ✅ FOMAML (Gradient-Based Fast Adaptation)
- [x] ✅ Reptile
- [ ] ⏳ Custom Meta-Environment Generators
- [ ] ⏳ Visualization Suite

---

## 🧑‍🔬 Who This Is For

This repo is meant for:
- Researchers
- Aspiring RL engineers
- Students building project portfolios
- Anyone obsessed with making agents *learn how to learn*

---

## 📜 License

MIT License. Use, study, modify freely. If you build on it, we’d love a mention or pull request!

