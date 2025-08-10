# **🚀 R2D2: Recurrent Experience Replay in Distributed Reinforcement Learning**

R2D2 is not just another RL agent — it's a deep dive into memory 🧠, a blend of recurrence and replay that lets your agent learn from long, tangled sequences of experience, conquering partial observability with a sharp mind and a steady hand.

# **🔍 What is R2D2 and How Powerful is It?**

R2D2 revolutionizes reinforcement learning by combining recurrent neural networks with experience replay, enabling agents to remember the past and learn from it efficiently. This approach shines brightest in environments where the present moment alone isn’t enough — where history whispers secrets only memory can reveal. 🌌

It scales across distributed architectures, blending stability and speed ⚡, and tackles complex tasks that stump simpler agents. R2D2 is the guardian of temporal dependencies, unlocking horizons where pure feedforward models falter. 🛡️

# **🎯 A Touch of PPO with R2D2 for Continuous Control**

This implementation spices up classic R2D2 with clipped Proximal Policy Optimization (PPO) style updates — elegantly marrying on-policy stability with off-policy efficiency. Designed for continuous action spaces, it harnesses stochastic policies with Gaussian distributions and recurrent LSTMs, carving a smooth path through the vast continuous action landscapes. 🌊

# **📦 What’s Inside?**

      PyTorch Implementation of R2D2’s actor-critic recurrent networks with LSTMs. 🔥
      
      Sequence Sampling & Burn-in Logic to warm up hidden states and ensure training stability. ♨️
      
      GAE-based PPO Loss functions tailored for recurrent policies. 📈
      
      TensorBoard Integration for real-time visualization. 📊
      
      plot.py — handy plotting scripts to transform logs into insights. 🎨
      
      Ready-to-run Jupyter Notebook encapsulating full training and evaluation. 📝

# **📉 Loss Graphs**

## **Policy Loss**

<img width="800" height="500" alt="Policy loss" src="https://github.com/user-attachments/assets/cee5d5ae-e837-4a94-aeca-7e493011e9b6" />

## **Value Loss**

<img width="800" height="500" alt="Val loss" src="https://github.com/user-attachments/assets/2a16a3f2-3cf3-416f-8882-d2c4f14effa2" />

## **Agent Loss**

<img width="800" height="500" alt="Agent loss" src="https://github.com/user-attachments/assets/ea3ec625-2f09-4e80-9783-b584711899e0" />


# **📝 Notes**


      Burn-in sequences are crucial to warm up the LSTM hidden states, preventing cold-start shocks. 🔥
      
      Orthogonal initialization with zero biases stabilizes early training epochs. 🧩
      
      This implementation is a fusion — leveraging the best of recurrent replay and PPO clipping, tuned for meta-RL challenges. ⚙️
      
      Expect some volatility early on; it’s the sign of learning sharpening its claws. 🐾

# **📚 References**

R2D2 Paper (Kapturowski et al., 2018)

PPO Paper (Schulman et al., 2017)

## **⚖️ License**

This project is licensed under the MIT License — free and open, like the curiosity that fuels us. ✨

### **🔮 Next Model in Line**

Ready to dive deeper? The next frontier is ANIL or LEAP — stay tuned for the next evolution in our meta-RL odyssey. 🚀
