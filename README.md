# **🦎 Reptile: Meta-Learning from Scratch**

Welcome to the Reptile implementation — the elegant, gradient-based meta-learning algorithm that’s all about fast adaptation through simple weight updates. This repo explores how agents can quickly learn new tasks by gently nudging their parameters closer to optimal solutions across a distribution of tasks.

## **🌱 What’s Inside This Reptile Branch?**

Full PyTorch implementation of Reptile from the ground up

Clean, well-documented Jupyter notebooks to visualize training and adaptation dynamics

Meta-episode runners and replay buffers tailored for Reptile’s inner-loop updates

Detailed explanations on how Reptile performs meta-updates without expensive second-order gradients

## **🧩 Why Reptile?**

Forget complex second-order derivatives — Reptile keeps it simple and elegant by performing meta-learning via repeated SGD on sampled tasks, then moving the initial parameters towards the adapted ones. This approach:

Is computationally efficient

Scales well to diverse task distributions

Encourages rapid adaptation on unseen tasks

Perfect for anyone wanting a straightforward yet powerful meta-learning algorithm that packs a punch.

## **🌟 How to Run and Experiment**

Clone the repo and switch to the reptile branch

Read the local README and comments in the Jupyter notebook

Run the training notebooks to see Reptile learn across multiple tasks

Tweak hyperparameters like meta learning rate, inner steps, and batch size to experiment with speed and stability of adaptation

Visualize the agent’s meta-adaptation curve and loss landscapes

## **🧭 Roadmap for Reptile Branch**

✅ Core Reptile Algorithm Implementation

✅ Meta Episode Runners & Replay Buffers

⏳ Advanced Scheduling and Learning Rate Strategies

⏳ Integration with Custom Meta-Environments

⏳ Visualization Tools for Meta-Learning Dynamics

### **🧑‍🔬 Who Should Dive In?**

Meta-RL researchers exploring gradient-based methods

Students eager to understand the mechanics of fast adaptation

Practitioners looking for efficient meta-learning baselines

Curious souls obsessed with how machines learn to learn

### **Losses Curve**

#### **Policy Loss**

<img width="800" height="501" alt="Policy_Figure_1" src="https://github.com/user-attachments/assets/42f8c286-1919-4c0a-ace2-a1d0675575f0" />

#### **Critic Loss**

<img width="800" height="500" alt="Figure_1" src="https://github.com/user-attachments/assets/9eaa3a41-bac7-4caf-97f4-3c942503e30d" />

#### **Agent Loss**


<img width="800" height="500" alt="Agent_Figure_1" src="https://github.com/user-attachments/assets/e02aca28-e10b-488b-9aa6-163d10adc490" />


### **📜 License**

MIT License — fork, tweak, and build on this freely. Just drop a ⭐ or PR if you find this useful!

