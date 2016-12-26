from sklearn.neural_network import MLPClassifier

# Just playing with a MLP classifier (multi-layer perception)
# http://scikit-learn.org/stable/modules/neural_networks_supervised.html

# TODO : transform into a clear function including a proper description
# of the solver, alpha , hidden layers terms

# X, training samples vector
training_set = [[0., 0.], [1., 1.]]

# Y target values for the training samples
target = [0, 1]

# MLP classifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

# We fit the model on the training data
clf.fit(training_set, target)

# We predict the label on new samples
print(clf.predict(([[2., 2.], [-1., -2.]])))
