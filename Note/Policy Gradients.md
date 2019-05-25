## Policy Gradients

### Indexing
- [Introduction](#Introduction)
- [References](#References)

---
### Introduction
*Different ways of Reinforcement Learning*
- Q learning, Deep Q Network: learn the reward, q-value
- Policy Gradients: do not analysis the reward, output the action directly

*Merits of Policy Gradients*
- The ability of choose actions in a sequent

*Updating of DQN and Policy Gradient*
- DQN: backpropagating the loss between real Q-value and evaluated Q-value 
- Policy Gradient: backpropagating to change the chosen propability of current action according to the reward.

*Details of updating*
- choose an action
- backpropagating and increase the chosen posibility of current action
- the bigger the reward is, the proportion of increase would be higher
---
### References
- [MorvanPYTHON](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/5-1-A-PG/)
---

