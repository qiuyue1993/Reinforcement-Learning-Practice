# Review of Reinforcement Learning

## Indexing:
- [Notes](#Notes)
- [Comments](#Comments)
- [References](#References)
---
## Notes:
### Reinforcement Learning Category
*Model-based and Model-free*
- Model-based: build the environment model, enable to learn in the simulated environment
- Model-free: do not build the environment model

*Propability-based and Value-based*
- Propability-based: Policy Gradients
- Value-based: Q-Learning, Sarsa
- Combined: Actor-critic

*Step-by-step Update and Turn Update*
- Step-by-step: Q-learning, Sarsa, Updated policy gradients
- Turn: Policy gradients, Monte-carlo learning
- **step-by-step is more efficient**

**On-policy and Off-policy**
- Off-policy enables the ability to learn from the past
- On-policy: sarsa
- Off-policy: Q-learning, Deep-Q-Network

### Q-Learning
- **Epsilon greedy**: decide to take the computed action with highest value or to take a random action
---
## Comments
- Model-based methods is better?!
- What is the model-based methods?

- Actor-Critic Model is better?
- **Policy Gradient** is difficult to learn??!!

---
## References
- [Morvan PYTHON](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/)
---
