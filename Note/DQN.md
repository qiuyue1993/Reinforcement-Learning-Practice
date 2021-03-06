## Deep Q Network

### Indexing:
- [Why Nerual Network](#Why-Neural-Network)
- [Update](#Update)
- [Algorithm](#Algorithm)
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
### Algorithm
**Deep Q-learning with experience replay**

Initialize replay memory D to capacity N

Initialize action-value function $Q$ with random weights $\theta$

Initialize target action-value function $\hat{Q}$ and weights $\theta^{-}=\theta$

**For** $episode = 1, M$ **do**

$\quad$ Initialize sequence $s_1 = \{x_1\}$ and preprocessed sequence $\phi_1 = \phi(s_1)$

$\quad$ **For** $t=1, T$ **do**

$\qquad$ With probability $\epsilon$ select a random action $a_t$

$\qquad$ otherwise select $a_t = argmax_aQ(\phi(s_t),a;\theta)$

$\qquad$ Execute action $a_t$ in enulator and observe reward $r_t$ and image $x_{t+1}$

$\qquad$ Set $s_{t+1} = s_t,a_t,x_{t+1}$ and preprocess $\phi_{t+1}=\phi(s_{t+1})$

$\qquad$ Store transition $(\phi_t,a_t,r_t,\phi_{t+1})$ in $D$

$\qquad$ Sample random minibatch of transitions $(\phi_j,a_j,r_j,\phi_{j+1})$ from $D$


$\qquad$ Set $y_j = r_j$ if episode terminates at step $j+1$

$\qquad$ Otherwise, set $y_j = r_j + \gamma max_{a^{'}} \hat{Q}(\phi_{j+1},a^{'};\theta^{-})$

$\qquad$ Perform a gradient descent step on $(y_j - Q(\phi_j,a_j;\theta))^{2}$ with respect to the network parameters $\theta$

$\qquad$ Every C steps reset $\hat{Q}=Q$

$\quad$ **End For**

**End For**

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
