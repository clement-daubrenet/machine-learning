import time


def execution_time(function_used):
    """
    Decoractor to calculate execution time of a function.
    :param function_used: function to evaluate.
    :return:
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function_used(*args, **kwargs)
        stop = time.time()
        return stop-start, result
    return wrapper
