def solve(base, exp):
    assert exp >= 0

    pows = [(0, 1), (1, base)]
    current_pow = 1
    while current_pow < exp:
        current_pow *= 2
        pows.append((current_pow, pows[-1][1] * pows[-1][1]))

    result = 1
    index = len(pows) - 1
    while exp > 0:
        if exp >= pows[index][0]:
            exp -= pows[index][0]
            result *= pows[index][1]
        else:
            index -= 1

    return result
