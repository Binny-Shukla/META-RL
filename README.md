# **🧩 CTX: Context-Aware Reinforcement Learning Framework**

Welcome to the CTX repo! This project builds on the foundations of PEARL with a focus on context-awareness and memory-enhanced meta-reinforcement learning. Below is a comprehensive README template designed to guide users through the repo structure, concepts, usage, and future plans.

# **📚 What is CTX?**

CTX (Context-Aware Reinforcement Learning) is a next-generation meta-RL model that integrates attention mechanisms and memory modules to better capture and utilize task context for faster, more robust adaptation across tasks.

# **⚡️ How Powerful Is CTX?**

Enhanced Context Understanding: Leveraging attention and memory to dynamically extract task-relevant information.

Improved Adaptability: Excels at meta-RL benchmarks requiring complex, temporally-extended tasks.

State-of-the-art Performance: Outperforms prior meta-RL approaches like PEARL on diverse multi-task environments.

# **🧠 How Does CTX Work?**

Context Memory Module: Stores and retrieves latent embeddings of past experiences to inform current decisions.

Attention Mechanism: Focuses on the most relevant parts of the context dynamically during policy evaluation.

Meta-Actor-Critic Architecture: Uses enriched context embeddings to adapt policy and value functions efficiently.

End-to-End Optimization: Trained with gradient-based methods for cumulative reward maximization across tasks.

# **🎯 Example Use Case**

Imagine a robotic arm performing a series of complex assembly tasks:

CTX enables the robot to remember key features from earlier tasks and selectively pay attention to these when learning new ones.

This leads to faster learning with less trial-and-error compared to baseline meta-RL models.

# **📉 Loss Curves & Metrics**

Track policy loss, value function loss, attention weights, and context embedding accuracy.

Visualize training progress using the provided plot.py script that processes TensorBoard logs to generate detailed plots.

Use the included Jupyter Notebook for a full step-by-step implementation and visualization walkthrough.

## **POLICY LOSS**

<img width="800" height="500" alt="CTX actor" src="https://github.com/user-attachments/assets/ff631ba4-fed2-47bc-b0d8-d4daaad0a779" />

## **CRITIC LOSS**


<img width="800" height="500" alt="CTX critic" src="https://github.com/user-attachments/assets/7cee3097-77ce-4e3f-b5f1-3f64edcbc014" />


# **📄 References**

      Original Paper: (Include paper title and authors if available)
      
      Related Work: PEARL (Rakelly et al.), Attention Mechanisms in RL
      
      TensorBoard for loss and metric visualization

# **🧩 Next Steps: Future Models**

Ongoing research prototypes exploring hybrid memory-attention models.

Further integration with transformers for extended task generalization.
