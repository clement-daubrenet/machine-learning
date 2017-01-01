# Based on : http://www.pyimagesearch.com/2016/10/17/stochastic-gradient-descent-sgd-with-python/


def stochastic_gradient_descent(data, loss, w, alpha):
    """
    Implementation of SGD algorithm. Pseudo-code for now.
    n.b: the difference with the usual gradient algorithm is the use 
    of "batches" and "next_training_batch" function. 
    :param data: the dataset
    :param loss:
    :param w:
    :param alpha: learning rate in the gradient descent algorithm 
    """
    while True:
        batch = next_training_batch(data, 256)
        w_gradient = evaluate_gradient(loss, batch, w)
        w += -alpha * w_gradient


def next_training_batch(data, size):
    return


def evaluate_gradient(loss, batch, w):
    return
