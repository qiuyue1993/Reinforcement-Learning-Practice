## Double DQN

### Indexing:
- [Double DQN vs Natural DQN](#Double-DQN-vs-Natural-DQN)
- [Algorithm](#Algorithm)
- [References](#References)

---
### Double DQN vs Natural DQN
**Problem of Natural DQN**
- DQN is based on the Q-learning, Q-learning have $Q_{max}$, the use of $Q_{max}$ would lead the **$Q_{real}$ to be overestimated**

**Double DQN**
- Do not use $Q_{max}$
- Make use of the two network of DQN 

---
### Algorithm
*Deep Q Learning*

$Q_{real}$: $\qquad  Y_t^{DQN}\equiv R_{t+1} + \gamma max_a Q(S_{t+1},a; \theta^{-})$ 

Updating: $\alpha (Q_{real} - Q_{eval})$ = $\alpha (R_{t+1} + \gamma Q(S_{t+1},a; \theta^{-}) - Q(s,a;\theta_t))$




---
### References
- [MorvanPYTHON](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/4-5-double_DQN/)
---
