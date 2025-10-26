from time import time

def duration(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        duration = end - start
        return {'time': duration, 'result': res}
    return wrapper

@duration
def timed_quicksort(arr, l=0, r=-1):
    return quicksort(arr, l=0, r=-1)

def quicksort(arr, l=0, r=-1):

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

    stack = [(l, r)]
    
    while stack:
        l, r = stack.pop()
        
        if l >= r:
            continue

        pivot_index = partition(arr, l, r)
        
        stack.append((l, pivot_index - 1))
        stack.append((pivot_index + 1, r))
    
    return arr

@duration
def timed_mergesort(arr):
    return mergesort(arr)

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    def merge(arr1, arr2):
        merged = []
        i, j = 0, 0
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        
        for i1 in range(i, len(arr1)):
            merged.append(arr1[i1])
        
        for j1 in range(j, len(arr2)):
            merged.append(arr2[j1])
        
        return merged
    
    n = len(arr)
    size = 1
    while size < n:
        for l in range(0, n, 2 * size):
            mid = min(l + size - 1, n - 1)
            r = min(l + 2 * size - 1, n - 1)
            
            arr_l = arr[l:mid + 1]
            arr_r = arr[mid + 1:r + 1]
            merged = merge(arr_l, arr_r)
            
            arr[l:l + len(merged)] = merged
        
        size *= 2
    
    return arr
