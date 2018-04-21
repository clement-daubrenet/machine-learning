import gym

parameters = {'learning_rate': 1e-3,
              'environment':  gym.make('CartPole-v0'),
              'goal_steps': 500,
              'score_requirement': 50,
              'initial_games': 10000}
