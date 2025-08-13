# **🦪 Probabilistic Embeddings for Actor-critic RL**

# **📖 What is PEARL?**

PEARL (Probabilistic Embeddings for Actor-critic RL) is a powerful reinforcement learning algorithm designed for fast adaptability across tasks. It utilizes probabilistic embeddings to enable meta-learning, making it highly efficient in multi-task environments.

# **🚀 How Powerful is PEARL?**

PEARL stands out for:

Fast adaptation to new tasks with minimal data.

Strong performance in meta-RL benchmarks.

Efficient utilization of experience via probabilistic context variables.

This makes PEARL a top choice for environments requiring quick generalization and robustness.

# **🛠️ How Does PEARL Work?**

Probabilistic Context Variable: Learns a latent representation of task context from previous experiences (via variational inference).

Meta-Actor-Critic Architecture: Uses the context variable as input for policy and value networks, enabling quick adaptation.

End-to-End Training: All components are optimized to maximize cumulative rewards across varied tasks.

# **💡 Example Use Case**

Imagine a robot learning to manipulate diverse objects:

PEARL enables the robot to rapidly adapt its strategy based on limited prior experience for each new object type—reducing retraining time and data needs.

# **📉 Loss Curves**
For best results:

Run plot.py to generate curves using tensorboard data.

Typical curves include actor loss, critic loss, and context encoder loss.

Use the notebook for full implementation and visualizations.

### **POLICY LOSS**

<img width="800" height="500" alt="pearl actor" src="https://github.com/user-attachments/assets/b7193326-bac7-4de4-8d1a-03f873e8796e" />

### **CRITIC LOSS**

<img width="800" height="500" alt="pearl critic" src="https://github.com/user-attachments/assets/c6864837-322c-4871-b37a-c951db7f78e3" />


# **🔗 References**

      Original Paper: "PEARL: Efficient Off-Policy Meta-RL via Probabilistic Context Variables" (Rakelly et al., 2019)
      
      arXiv: https://arxiv.org/abs/1903.08254

TensorBoard: For loss curve visualization

## **📝 Next Model: CTX**

      Upcoming: CTX meta-RL algorithm
      
      Stay tuned for the next readme!

### **📜 MIT License**

      Permission is hereby granted, free of charge, to any person obtaining a copy
      of this software and associated documentation files (the "Software"), to deal
      in the Software without restriction...
