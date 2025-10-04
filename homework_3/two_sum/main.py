def two_sum(arr, k):
    prev_numbers = {}
    for index1, v1 in enumerate(arr):
        v2 = k - v1
        if v2 in prev_numbers:
            index2 = prev_numbers[v2]
            return (index2, index1)
        if v1 not in prev_numbers:
            prev_numbers[v1] = index1
    return None