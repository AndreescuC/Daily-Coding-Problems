from math import factorial


def solve(n, m):
    return factorial(n + m - 2) / (factorial(n - 1) * factorial(m - 1))
