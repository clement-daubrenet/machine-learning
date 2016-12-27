from sklearn.neural_network import MLPClassifier

# Just playing with a MLP classifier (multi-layer perception)
# http://scikit-learn.org/stable/modules/neural_networks_supervised.html

# TODO: start a classifier MLP classifier and compare to scikit

class MLP:

    def __init__(self):
        self.clf = MLPClassifier(solver="lbfgs",
                                 alpha=1e-5,
                                 hidden_layer_sizes=(5, 2),
                                 random_state=1)

    def fit_with_mlp(self, sample, target):
        """
        Fiting using MLP classifier
        :param sample: input training sample
        e.g: sample = [[0., 0.], [1., 1.]]
        :param target: target for the given training sample
        e.g: output [0, 1]
        """
        self.clf.fit(sample, target)

    def predict_with_mlp(self, new_sample):
        """
        Predicting using MLP classifier
        :param new_sample: new sample to use for prediction
        e.g: new_sample = [[1., 0.], [0., 1.]]
        :return:
        """
        self.clf.predict(new_sample)


if __name__ == "__main__":
    mlp_classifier = MLP()
    mlp_classifier.fit_with_mlp([[0., 0.], [1., 1.]], [0., 1.])
    mlp_classifier.predict_with_mlp([[1., 0.], [0., 1.]])
