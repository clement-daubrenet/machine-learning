def activation(bias, weights, inputs):
    """
    Activation function for Perceptron.
    A good article here: https://medium.com/the-theory-of-everything/understanding-activation-functions-in-neural-networks-9491262884e0
    :param bias: the bias value often named "Beta0" in articles.
    :param weights: the list of weignts for the weighted sum.
    :param inputs: inputs from the training set.
    """
    activation += bias
    for index, weight in enumerate(weights):
        activation += weigh * inputs[index]
    return activation
