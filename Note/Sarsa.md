## Sarsa

### Indexing:
- [Abstract](#Abstract)
- [Sarsa Decision](#Sarsa-Decision)
- [Sarsa Update](#Sarsa-Update)
- [Differences between Sarsa and Q-Learning](Differences-between-Sarsa-and-Q-Learning)
- [References](#References)

---
### Abstract
- Use Q table to make decision
- Learn by updating Q table

---
### Sarsa Decision
- Use Q table to make decision
- Compare Q values of different actions from Q form, choose the action with the higher value
- Identical with Q-Learning

---
### Sarsa Update
- Update formulation

$(1) Q(s,a) \gets Q(s,a) + \alpha[r + \gamma Q(s^{'},a^{'}) - Q(s,a)]$

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
---
### Differences between Sarsa and Q-Learning
- The main difference is the update
- Sarsa is on-policy learning
- Q-Learning is off-policy learning

---
### References
- [MorvanPYTHON](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/3-1-A-sarsa/)
---
