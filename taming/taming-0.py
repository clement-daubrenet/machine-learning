# Snippets for GYM use.

import gym
import time

env = gym.make('CartPole-v0')


def random_moves():
    env.reset()
    for _ in range(100):
        env.render()
        env.step(env.action_space.sample()) # take a random action


def random_moves_with_done_break():
    for i_episode in range(20):
        # A simulation starts
        observation = env.reset()
        time.sleep(1)

        # Looping until the poll falls (done=True)
        for t in range(1000000):
            env.render()
            print(observation)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            
            # The poll falls
            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break


random_moves_with_done_break()
