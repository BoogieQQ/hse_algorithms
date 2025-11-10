from main import makeheap_n_log_n, makeheap_n
import random
import time

def is_min_heap(arr):
    n = len(arr)
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] < arr[i]:
            return False
        if right < n and arr[right] < arr[i]:
            return False
    return True

def test_makeheap_n_log_n_empty():
    arr = []
    result = makeheap_n_log_n(arr)
    assert result == []
    assert is_min_heap(result)

def test_makeheap_n_empty():
    arr = []
    result = makeheap_n(arr)
    assert result == []
    assert is_min_heap(result)

def test_makeheap_n_log_n_single():
    arr = [0]
    result = makeheap_n_log_n(arr)
    assert result == [0]
    assert is_min_heap(result)

def test_makeheap_n_single():
    arr = [0]
    result = makeheap_n(arr)
    assert result == [0]
    assert is_min_heap(result)

def test_makeheap_n_log_n_sorted_asc():
    arr = [0, 1, 2, 3, 4, 5]
    result = makeheap_n_log_n(arr)
    assert is_min_heap(result)
    assert sorted(result) == sorted(arr) # Проверка, что все эелементы начального массива вошли в кучу

def test_makeheap_n_sorted_asc():
    arr = [0, 1, 2, 3, 4, 5]
    result = makeheap_n(arr)
    assert is_min_heap(result)
    assert sorted(result) == sorted(arr)

def test_makeheap_n_log_n_sorted_desc():
    arr = [5, 4, 3, 2, 1, 0]
    result = makeheap_n_log_n(arr)
    assert is_min_heap(result)
    assert sorted(result) == sorted(arr)

def test_makeheap_n_sorted_desc():
    arr = [5, 4, 3, 2, 1]
    result = makeheap_n(arr)
    assert is_min_heap(result)
    assert sorted(result) == sorted(arr)

def test_makeheap_n_log_n_random():
    arr = [random.randint(0, 10) for _ in range(10)]
    result = makeheap_n_log_n(arr)
    assert is_min_heap(result)
    assert sorted(result) == sorted(arr)

def test_makeheap_n_random():
    arr = [random.randint(0, 10) for _ in range(10)]
    result = makeheap_n(arr)
    assert is_min_heap(result)
    assert sorted(result) == sorted(arr)

# Функция для сравнения времени
def cmp_performance():
    sizes = [100, 1000, 10_000, 100_000, 1_000_000]
    
    print("Cmp perfomance n_log_n vs n:")

    for size in sizes:
        arr = [random.randint(1, 100000) for _ in range(size)]
        
        start = time.time()
        makeheap_n_log_n(arr)
        time_n_log_n = time.time() - start
        
        start = time.time()
        makeheap_n(arr)
        time_n = time.time() - start
        
        ratio = time_n_log_n / time_n
        print(f"{size} \t {time_n_log_n:.6f} \t {time_n:.6f} \t {ratio:.2f}")
    
    
if __name__ == "__main__":
    cmp_performance()