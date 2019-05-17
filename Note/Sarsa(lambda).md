## Sarsa(lambda)

### Indexing:
- [Single Step Update and Round Update](Single-Step-Update-and-Round-Update)
- [Lambda](#Lambda)
- [References](#References)

---
### Single Step Update and Round Update
*Single Step Update*
- Update policy after every step
- Only the step before the reward can get updated

*Round Update*
- Update polify after every round
- Every step will get updated

---
### Lambda
- Lambda is a step decay value, the closer the step to the reward, the bigger the reward
- Lambda is between [0,1]
---
### References
- [MorvanPYTHON](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/3-3-A-sarsa-lambda/)
---
