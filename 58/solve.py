def solve(array, element):
    left = 0
    right = len(array) - 1

    while left < right:
        pivot = (left + right) // 2

        if element == array[pivot]:
            return pivot
        if element == array[right]:
            return right
        if element == array[left]:
            return left

        if element < array[pivot]:
            if element >= array[left] or array[pivot] < array[left]:
                right = pivot - 1
            else:
                left = pivot + 1
        else:
            if element <= array[right] or array[pivot] > array[right]:
                left = pivot + 1
            else:
                right = pivot - 1

    return -1
