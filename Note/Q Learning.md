## Q Learning

### Indexing:
- [Abstract](#Abstract)
- [Q-Learning Decision](#Q-Learning-Decision)
- [Q-Learning Update](#Q-Learning-Update)
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

$Q(s,a) \gets Q(s,a) + \alpha[r + \gamma max_{a^'}]$

---
### References
- [Morvan PYTHON](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/2-1-A-q-learning/)
---
