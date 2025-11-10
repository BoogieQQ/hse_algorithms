def makeheap_n_log_n(arr):
    arr = arr.copy()

    def shift_up(index):
        upper = (index - 1) // 2
        while index > 0 and arr[index] < arr[upper]:
            arr[index], arr[upper] = arr[upper], arr[index]
            index = upper
            upper = (index - 1) // 2

    for i in range(1, len(arr)):
        shift_up(i)
    
    return arr

def makeheap_n(arr):
    arr = arr.copy()

    def shift_down(index, size):
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            curent = index
            
            if left < size and arr[left] < arr[curent]:
                curent = left
            if right < size and arr[right] < arr[curent]:
                curent = right
                
            if curent == index:
                break
                
            arr[index], arr[curent] = arr[curent], arr[index]
            index = curent
    
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        shift_down(i, n)
    
    return arr