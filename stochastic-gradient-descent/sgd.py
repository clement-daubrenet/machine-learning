# Based on : http://www.pyimagesearch.com/2016/10/17/stochastic-gradient-descent-sgd-with-python/
import numpy as np


def stochastic_gradient_descent(data, labels, loss, w, alpha):
    """
    Implementation of SGD algorithm. Pseudo-code for now.
    n.b: the difference with the usual gradient algorithm is the use
    of "batches" and "next_training_batch" function.
    :param data: the training dataset vectors
    :param labels: the labels associated to the training dataset vectors
    :param loss:
    :param w:
    :param alpha: learning rate in the gradient descent algorithm
    """
    while True:
        batch = next_training_batch(data, labels, 256)
        w_gradient = evaluate_gradient(loss, batch, w)
        w += -alpha * w_gradient


def next_training_batch(X, y, batch_size):
    """
    :param X: training dataset of vectors
    :param y: class labels associated with each of the training data points
    :param batch_size: size of data sub-batches returned
    """
    # looping "in batches" over X, the training dataset
    for i in np.arange(0, X.shape[0], batch_size):
        # yield a tuple (dataset, label) of the right size
        yield (X[i: i+batch_size], y[i: i+batch_size])


def evaluate_gradient(loss, batch, w):
    return

batch = next_training_batch(np.array([[0, 0, 0], [1, 1, 1]]), np.array([0, 1]), 2)
for element in batch:
    print(element)
