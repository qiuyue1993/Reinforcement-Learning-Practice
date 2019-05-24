## Prioritized Experience Replay DQN

### Indexing:
- [Why Prioritized Experience Replay](Why-Prioritized-Experience-Replay)
- [Prioritized Replay Algorithm](#Prioritized Replay Algorithm)
- [SumTree Valid Sampling](#SumTree-Valid-Sampling)
- [Memory](#Memory)
- [Updating](#Updating)
- [References](#References)

---
### Why Prioritized Experience Replay
- Sometimes, the important memories could be very limited,
- To learn from important memory

---
### Prioritized Replay Algorithm
- Instead of random sampling from memory, **choose memory samples according to their priority**
- **TD-error**: the sample with higher difference between $Q_{real}$ and $Q_{eval}$ have higher priority
- **How to sample according to the priority**:  Use the SumTree

---
### SumTree Valid Sampling
*SumTree*
- Leaf: priority for every sample
- Root: sum priority of all samples

*Sampling*
- $n = (sum of priority)/batch_size$
- Choose $n$ section of priority
- Choose a priority from every section randomly
- Search the SumTree

---
### References
- [MorvanPYTHON](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/4-6-prioritized-replay/)
---
