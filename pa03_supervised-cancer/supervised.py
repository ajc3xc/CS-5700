#!/usr/bin/python3
# -*- coding: utf-8 -*-
# You can import anything standard python, numpy, or pandas.
from typing import cast, Tuple
import numpy as np
import numpy.typing as npt
import pandas as pd  # type: ignore
from sklearn.ensemble import RandomForestClassifier  # type: ignore


def import_data(filename: str) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.int64]]:
    """
    Imports csv data, processes it, and returns it ready for learning!

    Parameters
    ----------
    filename : str
        Either the train or test data in this directory.

    Returns
    -------
    data : np.ndarray
        The X data vectors.
    target : np.ndarray
        The single y colum vector.
    """
    df = pd.read_csv(filename)

    # Assuming the last column is the target variable
    X = df.iloc[:, :-1].values.astype(np.float64)
    y = df.iloc[:, -1].values.astype(np.int64)

    return X, y


class MyLearner:
    def __init__(
        self,
    ) -> None:
        self.learning_rate: float = 0.01
        self.iterations: int = 1000
        self.lambda_param: float = 0.1  # Regularization parameter
        self.weights: npt.NDArray[np.float64] = np.zeros(0, dtype=np.float64)
        self.bias: float = 0.0
        self.mean: npt.NDArray[np.float64] = np.zeros(0, dtype=np.float64)
        self.std: npt.NDArray[np.float64] = np.zeros(0, dtype=np.float64)

    def _sigmoid(self, z: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        return 1 / (1 + np.exp(-z))

    def _feature_scaling(
        self, data: npt.NDArray[np.float64]
    ) -> npt.NDArray[np.float64]:
        if (
            self.mean.size == 0 or self.std.size == 0
        ):  # Check if mean and std are initialized
            self.mean = np.mean(data, axis=0)
            self.std = np.std(data, axis=0)
        return (data - self.mean) / self.std

    # generate weights for model from test data
    def fit(self, data: npt.NDArray[np.float64], target: npt.NDArray[np.int64]) -> None:
        data_scaled: npt.NDArray[np.float64] = self._feature_scaling(data)
        n_samples, n_features = data_scaled.shape
        self.weights = np.zeros(n_features, dtype=np.float64)
        self.bias = 0.0

        for _ in range(self.iterations):
            model: npt.NDArray[np.float64] = (
                np.dot(data_scaled, self.weights) + self.bias
            )
            predictions: npt.NDArray[np.float64] = self._sigmoid(model)

            dw: npt.NDArray[np.float64] = (1 / n_samples) * np.dot(
                data_scaled.T, (predictions - target)
            ) + (self.lambda_param / n_samples) * self.weights
            db: float = (1 / n_samples) * np.sum(predictions - target)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    # generate predicted y values for inputted test data
    def predict(self, data: npt.NDArray[np.float64]) -> npt.NDArray[np.int64]:
        data_scaled: npt.NDArray[np.float64] = self._feature_scaling(data)
        model: npt.NDArray[np.float64] = np.dot(data_scaled, self.weights) + self.bias
        predictions: npt.NDArray[np.float64] = self._sigmoid(model)
        class_labels: npt.NDArray[np.int64] = np.array(
            [1 if i > 0.5 else 0 for i in predictions], dtype=np.int64
        )
        return class_labels


def main() -> None:
    X, y = import_data("GSE73002_breast_cancer_train.csv")
    my_learner = MyLearner()
    my_learner.fit(data=X, target=y)

    # Validation test
    my_results = my_learner.predict(data=X)
    your_score = list(y == my_results).count(True) / len(y)
    print("Testing on the train set (statistical cheating):", your_score)

    # Real test of generalization
    X, y = import_data("GSE73002_breast_cancer_test.csv")
    my_results = my_learner.predict(data=X)
    your_score = list(y == my_results).count(True) / len(y)
    print("Testing on the test set (fair):", your_score)


if __name__ == "__main__":
    main()
