#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: udemy
"""

import gym

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

env = gym.make('CartPole-v1')

num_episodes = 1000

steps_total = []
rewards_total = []

for i_episode in range(num_episodes):
    
    state = env.reset()
    
    step = 0
    #for step in range(100):
    while True:
        
        step += 1
        
        action = env.action_space.sample()
        
        new_state, reward, done, info = env.step(action)

        print(reward, done)

        #print(new_state)
        #print(info)
        
        env.render()
        
        if done:
            steps_total.append(step)
            rewards_total.append(reward)
            print("Episode finished after %i steps" % step )
            print("Episode finished reward %i steps" % reward )
            break
        
        
print("Average number of steps: %.2f" % (sum(steps_total)/num_episodes))
#plt.plot(steps_total)
#plt.show()
#plt.plot(rewards_total)
#plt.show()
