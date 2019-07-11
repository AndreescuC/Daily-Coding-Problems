from solve import solve


def main():
    for index, multiset in enumerate(get_tests()):
        print("Test %d\nMultiset: %s\n Can it be split: %s\n\n" % (index, multiset.__repr__(), solve(multiset)))


def get_tests():
    return [
        [2, 7, 11, 3, 9, 3, 5],  # True
        [2, 7, 11, 3, 9, 3],  # False
        [15, 5, 20, 10, 35, 15, 10],  # True
        [15, 5, 20, 10, 35]  # False
    ]


if __name__ == '__main__':
    main()

