import random
import numpy as np
from statistics import mean, median
from collections import Counter
import cart_pole_model
import config


env = config.parameters['environment']


def get_training_sample():
    """
    Generating random games and keeping the best performances to train our model later.
    :return:
    """

    # Initial containers
    env.reset()
    training_data = []
    scores = []
    accepted_scores = []

    # Generating random initial games
    for _ in range(config.parameters['initial_games']):
        score = 0
        game_memory = []
        prev_observation = []
        for _ in range(config.parameters['goal_steps']):
            action = random.randrange(0, 2)
            observation, reward, done, info = env.step(action)
          
            if len(prev_observation) > 0:
                game_memory.append([prev_observation, action])
            prev_observation = observation
            score += reward
            if done:
                break

        # If the score is above the requirement, we keep this game to train our model.
        if score >= config.parameters['score_requirement']:
            accepted_scores.append(score)
            for data in game_memory:
                if data[1] == 1:
                    output = [0, 1]
                elif data[1] == 0:
                    output = [1, 0]
                training_data.append([data[0], output])

        env.reset()
        scores.append(score)
      
    training_data_save = np.array(training_data)
    np.save('./saved_models/saved.npy', training_data_save)

    print('Average accepted score:', mean(accepted_scores))
    print('Median:', median(accepted_scores))
    print(Counter(accepted_scores))

    return training_data


def train_model(training_data):
    """
    Training the model: passing best performance games to feed the network.
    :param training_data: collection of best performance games.
    :return:
    """
    X = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]), 1)
    y = [i[1] for i in training_data]
    model = cart_pole_model.neural_network_model(input_size=len(X[0]))

    model.fit({'input': X},
              {'targets': y},
              n_epoch=5, snapshot_step=500, show_metric=True, run_id='openaistuff')

    return model


def test_model(model):
    """
    Testing the model: ask our model to play games.
    :param model:
    :return:
    """
    env.reset()
    scores = []
    choices = []
    for each_game in range(10):
        score = 0
        game_memory = []
        prev_obs = []
        env.reset()
        for _ in range(config.parameters['goal_steps']):
            env.render()
            if len(prev_obs) == 0:
                action = random.randrange(0, 2)
            else:
                action = np.argmax(model.predict(prev_obs.reshape(-1, len(prev_obs), 1))[0])
            choices.append(action)
            new_observation, reward, done, info = env.step(action)
            prev_obs = new_observation
            game_memory.append([new_observation, action])
            score += reward
            if done:
                break
        scores.append(score)

        print('Average Score', sum(scores) / len(scores))
        print('Choice 1: {}, Choice 2: {}'.format(choices.count(1) / len(choices), choices.count(0) / len(choices)))


test_training_data = get_training_sample()
trained_model = train_model(test_training_data)
test_model(trained_model)
