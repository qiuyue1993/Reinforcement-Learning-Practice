## Introduction

### Indexing:
- [Class of Reinforcement Learning](Class-of-Reinforcement-Learning)
- [RL Methods](#RL-Methods)
- [References](#References)

---
### Class of Reinforcement Learning
#### Choose action based on value
- Q learning
- Sarsa
- Deep Q Neetwork

#### Choose action directly
- Policy Gradients

#### Image environment and learn from it
- Model based RL

---
### RL Methods
#### Model-free and Model-based methods
*Model-free methods*
- do not try to understand environment
- Examples: Q learning, Sarsa, Policy Gradients

*Model-based methods*
- Learn representation model for environment
- Examples: AlphaGo

#### Probability-based and Value-based RL
*Probability-based methods*
- Output probabilities of each action, act based on probabilities
- Examples: Policy Gradients

*Value-based methods*
- Output values of each action, choose the action with highest value
- Examples: Q learning, Sarsa

*Actor-Critic*
- Probability and Value based

#### Monte-Carlo update and Temporal-Difference update
*Monte-Carlo update*
- Update after gameover
- Examples: Monte-carlo learning, policy gradients

*Temporal-Difference update*
- Update after every action
- Examples: Qlearning, Sarsa, Actor-Critic
- As temporal-difference update is more efficient, it is more popular than Monte-Carlo update

#### On-Policy and Off-Policy Methods
*On-Policy*
- Examples: Sarsa, Sarsa lambda

*Off-Policy*
- Can learn from past or others
- Examples: Q learning, Deep-Q-Network

---
### References
- [Morvan PYTHON](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/1-1-A-RL/)
---
