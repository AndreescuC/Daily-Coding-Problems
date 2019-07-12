from solve import solve, solve_wo_div


def main():
    for index, array in enumerate(get_tests()):
        print(
            "Test %d\nFor array %s\nSolution with division: %s\nSolution without division: %s\n\n" %
            (index, array, solve(array), solve_wo_div(array))
        )


def get_tests():
    return [
        [1, 2, 3, 4, 5],
        [2, 3, 4],
        [0, 2, 3, 4]
    ]


if __name__ == '__main__':
    main()
