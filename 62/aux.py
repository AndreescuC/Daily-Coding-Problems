from solve import solve


def main():
    for index, test in enumerate(get_tests()):
        n, m = test
        print("Test %d\n Give a %d x %d matrix, ways to reach lower-right corner: %d\n" % (index, n, m, solve(n, m)))


def get_tests():
    """
    format (N, M)
    """
    return [
        (2, 5),
        (2, 2),
        (5, 5),
        (5, 1)
    ]


if __name__ == '__main__':
    main()
