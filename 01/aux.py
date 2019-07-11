from solve import solve


def main():
    for index, test in enumerate(get_tests()):
        array, target_sum = test
        print(
            "Test %d\nFor array %s\nSum %d\nPair found: %s\n\n" %
            (index, array.__repr__(), target_sum, solve(array, target_sum).__repr__())
        )


def get_tests():
    """
    format: (array, the target sum)
    """
    return [
        ([1, 2, 3, 4], 3),
        ([1, 2, 3, 4], 12),
        ([10, 15, 3, 7], 17),
        ([10, 15, 3, 7], 9),
        ([10, 15, 3, 7, 18, 4, 33, 12, 10, 15], 9),
        ([10, 15, 3, 7, 18, 4, 33, 12, 10, 15], 31),
        ([10, 15, 3, 7, 18, 4, 33, 12, 10, 15], 25),
        ([10, 15, 3, 7, 18, 4, 33, 12, 10, 15], 99)
    ]


if __name__ == '__main__':
    main()
