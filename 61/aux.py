from solve import solve


def main():
    for index, test in enumerate(get_tests()):
        base, exp = test
        print("Test %d.\nFor base %d and exp %d, result is %d\n" % (index, base, exp, solve(base, exp)))


def get_tests():
    """
    format: (base, exponent)
    """
    return [
        (2, 12),
        (2, 13),
        (2, 9),
        (3, 4),
        (6, 1),
        (6, 0),
        (6, 3)
    ]


if __name__ == '__main__':
    main()
