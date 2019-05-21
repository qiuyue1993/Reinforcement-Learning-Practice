## Deep Q Network

### Indexing:
- [Why Nerual Network](#Why-Neural-Network)
- [Update](#Update)
- [Algorithm](#Algotrithm)
- [Important ideas of DQN](Important-ideas-of-DQN)
- [References](#References)

---
### Why Nerual Network
- Memory Efficiency: For real application, the scale of state could be huge
- Time Efficiency: time to explore Q-table

**Steps for NN**
- Input State, Output Q-value for every action
- Choose the action with the max Q-value
- Learn by RL updating policy

---
### Update
- Q-prediction for every action
- Q-real for every action
- Update: new params = old params + $\alpha$(Q-real - Q-prediction)
---
### Algotrithm
**Deep Q-learning with experience replay**

Initialize replay memory D to capacity N

Initialize action-value function $Q$ with random weights $\theta$

Initialize target action-value function $\hat{Q}$ and weights $\theta^{-}=\theta$

**For** episode = 1, M **do**
  Initialize sequence $s_1 = {x_1}$ and preprocessed sequence $\phi_1 = \phi(s_1)$



---
### Important ideas of DQN
**Experience replay**
- Extract past experiments to learn randomly while updating the network
- Break the relevance between different experiences, making the network more efficient

**Fixed Q-targets**
- Also a mechanism to break the relevance between different experiences
- Use two networks with the same structures and different parameters
- Network for Q-prediction: with newest parameters
- Network for Q-real: with old parameters 
 
---
### References
- [MorvanPYTHON](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/4-1-A-DQN/)
---
