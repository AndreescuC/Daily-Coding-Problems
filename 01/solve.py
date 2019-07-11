def solve(array, target_sum):
    pairing_dic = set()

    for element in array:
        if element in pairing_dic:
            return True
        pairing_dic.add(target_sum - element)

    return False
