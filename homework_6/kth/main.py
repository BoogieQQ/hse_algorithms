def quickselect(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return None
    k_smallest = len(arr) - k
    return _quickselect(arr, 0, len(arr) - 1, k_smallest)

def _quickselect(arr, l, r, k_smallest):
    
    def partition(arr, l, r):
        pivot = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[r] = arr[r], arr[i]

        return i

    if not arr:
        return arr
    
    r = len(arr) - 1 if r == -1 else r
    
    pivot_index = partition(arr, l, r)
    
    if k_smallest == pivot_index:
        return arr[k_smallest]
    elif k_smallest < pivot_index:
        return _quickselect(arr, l, pivot_index - 1, k_smallest)
    else:
        return _quickselect(arr, pivot_index + 1, r, k_smallest)
