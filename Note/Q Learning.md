## Q Learning

### Indexing:
- [Abstract](#Abstract)
- [Q-Learning Decision](#Q-Learning-Decision)
- [Q-Learning Update](#Q-Learning-Update)
- [Explanation for Gamma](#Explanation-for-Gamma)
- [References](#References)

---
### Abstract
- Use Q form to make decision
- Learn by update Q form

---
### Q-Learning Decision
- Use Q form to make decision
- Compare Action Q value from Q form, choose the higher one

---
### Q-Learning Update
- Update the Q table after taken an action, arrived at a new state 
- Update formulation:

$(1) Q(s,a) \gets Q(s,a) + \alpha[r + \gamma max_{a^{'}Q(s^{'},a^{'}) - Q(s,a)}]$

---
### Q-Learning Algorithm
```
Initialize Q(s,a) arbitrarily
Repeat (for each episode):
  Initialize s
  Repeat (for each step of episode):
    Choose a from s using policy derived from Q (e.g., e-greedy)
    Take action a, observe r, s'
    Update Q(s,a) using equation (1)
    s = s'
  until s is terminal
```

- $\epsilon -greedy$ is a decision strategy, when epsilon = 0.9, there's 0.9 probability to make an option and 0.1 for random
- alpha: learning rate
- gamma: decay for future rewards

---
### Explanation for Gamma
- The smaller the gamma is, the robot will concentrate on the close reward
- The bigger the gamma is, the robot will perceive the far reward
---
### References
- [Morvan PYTHON](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/2-1-A-q-learning/)
---
