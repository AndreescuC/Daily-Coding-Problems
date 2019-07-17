from solve import car, cdr


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def get_tests():
    return [
        (car(cons(1, 2)), 1),
        (cdr(cons(1, 2)), 2)
    ]


def main():
    for index, test in enumerate(get_tests()):
        result, expected_result = test
        print("Test %d: " % index, end='')
        if result == expected_result:
            print("Success")
        else:
            print("Fail. Expected %d, given %d", expected_result, result)


if __name__ == '__main__':
    main()
