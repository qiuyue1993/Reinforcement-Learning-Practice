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
- **Decay rate beta**: the decay rate for future reward
- **Learning rate alpha**

*Algorithm*
- Initialize Q table
- For each episode, repeat
- Initialize environment $s$
- For each step of episode, repeat
- Choose an action $a$ using policy (Action with highest value or random)
- Take action $a$, observe the next environment and value
- Update the value of $(s,a)$ 
- Update $s$
- End episode

### Sarsa
- On-policy learnng
- Take two action in each step
- Q-Learning is more greedy than sarsa

*Sarsa lambda*
- Lambda is a decay value for reward those steps close to the end goal
- Requires to save the **trace**

### Deep Q Network
- Introduce NN for computing the **value of different actions given an enviroment state**

*Powerful components*
- Experience replay
- Fixed Q-targets
- Both of each can help breaking the dependency between different data

*Double DQN*
- Prevent from overestimate occuring in DQN

*Prioritized Experience replay*
- The reward is little in DQN
- This replay is to value the experience making the important experience been replayed more
- Utilizing the sum tree and memory

*Dueling DQN*
- Break the value of action to a value of state and a value of action
- This helps a lot while choosing action do not have much influence on the result

### Policy Gradients
- Propability-based
- Turn Update
- Enables to choose action sequence, not just discrete actions 
- Not really need the epsilon-greedy

*Core Idea*
- Backpropagating to increase the propabilities to be chosen of actions with high reward but low propabilities

*Algorithm*

<img src="https://github.com/qiuyue1993/Reinforcement-Learning-Practice/blob/master/Images/Policy-Gradient_Base-Algorithm.png" width="600" hegiht="400" align=center/>

*Coding Process*
- store_transition(observation, action, reward): save the transition of every step
- discount and norm reward of every turn
---
## Comments
- Model-based methods is better?!
- What is the model-based methods?

- Actor-Critic Model is better?
- **Policy Gradient** is difficult to learn??!!

- For policy gradient, updating by turn means that agent won't learn while stepping?!

---
## References
- [Morvan PYTHON](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/)
---
