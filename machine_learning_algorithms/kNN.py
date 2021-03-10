from collections import Counter
import numpy as np


class KNearestNeighbor:

    def __init__(self, k=5):
        self.k = k

    def fit(self, X, y):
        self._X_train = X
        self._y_train = y
        return self

    def predict(self, X_predict):
        distances = [np.sum((x_train - X_predict) ** 2) ** 0.5 for x_train in self._X_train]
        topK_index = np.argsort(distances)[:self.k]
        topK = self._y_train[topK_index]
        return Counter(topK).most_common(1)[0][0]
