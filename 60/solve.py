import numpy as np


def solve(multiset):
    s = sum(multiset)
    if s % 2 != 0:
        return False

    return exists_subset_sum(multiset, s // 2)


def exists_subset_sum(array, s):
    array = [0] + array
    mat = np.array([[False for _ in range(s + 1)] for _ in range(len(array))])

    mat[0, :] = True

    for i in range(1, len(array)):
        for j in range(1, s + 1):

            if array[i] > s:
                mat[i][j] = mat[i - 1][j]
                continue

            mat[i][j] = mat[i - 1][j] or mat[i - 1][s - array[i]]

    return mat[-1][-1]
