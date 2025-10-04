def anagrams(arr):
    sorted_arr = [''.join(sorted(s)) for s in arr]
    str_set = list(set(sorted_arr))

    ans = [[] for _ in range(len(str_set))]
    for sorted_str, default_str in zip(sorted_arr, arr):
        str_group = str_set.index(sorted_str)
        ans[str_group].append(default_str)

    return ans
