import numpy as np


def solve(array):
    array = np.array(array)
    zero_elements = np.argwhere(array == 0)

    if len(zero_elements) == 1:
        zero_at = zero_elements[0][0]
        result = [0] * len(array)
        result[zero_at] = np.prod(array[np.arange(len(array)) != zero_at])
        return result

    if len(zero_elements) > 1:
        return [0] * len(array)

    prod = np.prod(array)
    return [prod // x if x != 0 else prod for x in array]


def solve_wo_div(array):
    l = len(array)
    increasing_prod = [1] * l
    decreasing_prod = [1] * l

    for index in range(l - 1):
        increasing_prod[index + 1] = increasing_prod[index] * array[index]
        decreasing_prod[l - index - 2] = decreasing_prod[l - index - 1] * array[l - index - 1]

    return [x * y for x, y in zip(increasing_prod, decreasing_prod)]
