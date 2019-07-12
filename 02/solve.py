from operator import mul
from functools import reduce


def solve(array):
    prod = reduce(mul, array, 1)
    return [prod // x for x in array]


def solve_wo_div(array):
    l = len(array)
    increasing_prod = [1] * l
    decreasing_prod = [1] * l

    for index in range(l - 1):
        increasing_prod[index + 1] = increasing_prod[index] * array[index]
        decreasing_prod[l - index - 2] = decreasing_prod[l - index - 1] * array[l - index - 1]

    return [x * y for x, y in zip(increasing_prod, decreasing_prod)]
