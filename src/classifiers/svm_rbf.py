from classifiers import abstract_svm as asvm

class SVMRBF(asvm.AbstractSVM):

    def __repr__(self):
        return "<SVMRBF>"

    def __str__(self):
        return "SVM RBF"

    def train(self, labels, train_set):
        super(SVMRBF, self).train_helper(labels, train_set, 'rbf')

