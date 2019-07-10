from solve import solve
from random import choice


def rotate(array, rotations):
    for _ in range(rotations):
        pivot = choice(range(len(array)))
        array = array[pivot:] + array[:pivot]

    return array


def main():
    test_index = 1

    for array, rotations, element in get_tests():
        array = list(set(array))
        array.sort()
        array = rotate(array, rotations)

        print(
            "Test %d: Array: %s\nSearching for %d\nFound at index %d\n\n" %
            (test_index, array.__repr__(), element, solve(array, element))
        )
        test_index += 1


def get_tests():
    """
    format: (tested array, number of rotations, searched element)
    """
    return [
        ([1, 2, 12, 4, 5, 19, 7, 10, 14, 17, 90], 12, 2),
        ([2, 3, 6, 18, 23, 51, 23, 21, 41, 12, 54, 129, 54, 98, 32], 14, 23),
        (list(range(24)), 10, choice(range(24))),
        (list(range(30)), 10, choice(range(24))),
        (list(range(9)), 10, choice(range(24))),
        (list(range(24)), 10, 44),
        (list(range(30)), 10, 30),
        (list(range(9)), 10, -5)
    ]


if __name__ == '__main__':
    main()
