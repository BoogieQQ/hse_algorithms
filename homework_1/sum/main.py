def find_max(arr):
    if len(arr) == 0:
        return 0
    arr = list(map(int, arr.split()))

    odd_counter, min_odd = 0, None
    for e in arr:
        if e % 2 == 0:
            continue
        odd_counter += 1
        if min_odd is None or e < min_odd:
            min_odd = e
        
    if odd_counter % 2 == 1:
        arr.remove(min_odd)
    
    return sum(arr)
