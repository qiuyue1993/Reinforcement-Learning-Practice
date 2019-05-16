import numpy as np
import pandas as pd
import time

def build_q_table(n_states, actions):
  
N_STATES=6
ACTIONS=['left','right']
EPSILON=0.9
ALPHA=0.1
GAMMA=0.9
MAX_EPISODES=13
FRESH_TIME=0.3

