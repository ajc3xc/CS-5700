#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import numpy.typing as npt

# Remember: don't import or use anything else besides base python and numpy!


def n_choose_2(n: int) -> int:
    "Returns the value of n choose 2 as an int"
    # C(n, k) = n!/k!(n-k)!, k = 2, so C(n, 2) = n!/2!(n-2)! = n(n-1)/2! = n(n-1)/2
    return n * (n - 1) // 2


# TODO fix typing for char/int inside ndarray
def contingency_table(
    labels_true: npt.NDArray[np.int64], labels_pred: npt.NDArray[np.int64]
) -> npt.NDArray[np.int64]:
    "Returns the contingency table as an np array of integers"
    # print('delete this and write your code')

    unique_true_labels = np.unique(labels_true)
    unique_pred_labels = np.unique(labels_pred)

    # Initialize contingency matrix
    contingency_matrix = np.zeros(
        (len(unique_true_labels), len(unique_pred_labels))
    ).astype(np.int64)

    # Fill the contingency matrix
    for i, true in enumerate(unique_true_labels):
        for j, pred in enumerate(unique_pred_labels):
            contingency_matrix[i, j] = np.sum(
                (labels_true == true) & (labels_pred == pred)
            )

    # Display the matrix
    return contingency_matrix


def confusion_table(contingency: npt.NDArray[np.int64]) -> npt.NDArray[np.int64]:
    "Returns the confusion matrix as an np array of integers"
    # Convert the input matrix to a NumPy array for easy manipulation

    # seems stupid but it works
    # number of samples = number of items in confusion array
    n_samples = np.sum(contingency)

    n_c = np.ravel(contingency.sum(axis=1))
    n_k = np.ravel(contingency.sum(axis=0))
    sum_squares = (contingency**2).sum()
    print(sum_squares)
    print(n_samples**2)
    Confusion_Matrix = np.empty((2, 2), dtype=np.int64)
    Confusion_Matrix[1, 1] = sum_squares - n_samples
    Confusion_Matrix[0, 1] = contingency.dot(n_k).sum() - sum_squares
    Confusion_Matrix[1, 0] = contingency.transpose().dot(n_c).sum() - sum_squares
    Confusion_Matrix[0, 0] = (
        n_samples**2 - Confusion_Matrix[0, 1] - Confusion_Matrix[1, 0] - sum_squares
    )
    return Confusion_Matrix


def rand(confusion: npt.NDArray[np.int64]) -> float:
    "Returns the Rand Index as a float"
    numerator = confusion.diagonal().sum()
    denominator = confusion.sum()

    if numerator == denominator or denominator == 0:
        # Special limit cases: no clustering since the data is not split;
        # or trivial clustering where each document is assigned a unique
        # cluster. These are perfect matches hence return 1.0.
        return 1.0
    else:
        return float(numerator / denominator)


if __name__ == "__main__":
    # This is a demonstration of how your functions could be used.
    # They should match the ones from sklearn and scipy,
    # but not use those as imports!
    from scipy.special import comb  # type: ignore
    from sklearn.metrics.cluster import contingency_matrix  # type: ignore
    from sklearn.metrics.cluster import pair_confusion_matrix
    from sklearn.metrics.cluster import rand_score

    labels_true = np.array(
        [
            "x",
            "x",
            "x",
            "x",
            "x",
            "o",
            "x",
            "o",
            "o",
            "o",
            "o",
            "v",
            "x",
            "x",
            "v",
            "v",
            "v",
        ]
    )
    labels_pred = np.array([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3])

    print("Your n_choose_2 with n=7\n", n_choose_2(7))
    print("SciPy's comb with n=7, k=2\n", comb(7, 2))

    contingency = contingency_table(labels_true, labels_pred)
    print("\nYour contingency:\n", contingency)
    print("sklearn's contingency:\n", contingency_matrix(labels_true, labels_pred))

    confusion = confusion_table(contingency)
    print("\nYour confusion:\n", confusion)
    print("sklearn's confusion:\n", pair_confusion_matrix(labels_true, labels_pred))

    print("\nYour rand:", rand(confusion))
    print("sklearn's rand:", rand_score(labels_true, labels_pred))
