def activation(bias, weights, inputs):
    """
    Activation function for Perceptron. 
    Its a step function: if the weigted sum is positive, returns 1. If not, returns 0.
    A good article here: https://medium.com/the-theory-of-everything/understanding-activation-functions-in-neural-networks-9491262884e0
    An application there: https://machinelearningmastery.com/implement-perceptron-algorithm-scratch-python/
    :param bias: the bias value often named "Beta0" in articles.
    :param weights: the list of weignts for the weighted sum.
    :param inputs: inputs from the training set.
    """
    activation += bias
    for index, weight in enumerate(weights):
        activation += weigh * inputs[index]
    if activation>=0:
        return 1
    return 0 
