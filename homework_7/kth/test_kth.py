import pytest
from main import my_kth, heapq_kth

def test_example1():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    my_result = my_kth(nums, k)
    heapq_result = heapq_kth(nums, k)
    assert my_result == 5
    assert heapq_result == 5
    assert my_result == heapq_result

def test_example2():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    my_result = my_kth(nums, k)
    heapq_result = heapq_kth(nums, k)
    assert my_result == 4
    assert heapq_result == 4
    assert my_result == heapq_result

def test_single_element():
    nums = [0]
    k = 1
    my_result = my_kth(nums, k)
    heapq_result = heapq_kth(nums, k)
    assert my_result == 0
    assert heapq_result == 0
    assert my_result == heapq_result

def test_kth_max():
    nums = [0, 1, 2, 3, 4, 5, 6]
    k = 1
    my_result = my_kth(nums, k)
    heapq_result = heapq_kth(nums, k)
    assert my_result == 6
    assert heapq_result == 6
    assert my_result == heapq_result

def test_kth_min():
    nums = [0, 1, 2, 3, 4, 5, 6]
    k = 7
    my_result = my_kth(nums, k)
    heapq_result = heapq_kth(nums, k)
    assert my_result == 0
    assert heapq_result == 0
    assert my_result == heapq_result

def test_duplicate():
    nums = [0, 0, 1, 1, 2, 2]
    k = 4
    my_result = my_kth(nums, k)
    heapq_result = heapq_kth(nums, k)
    assert my_result == 1
    assert heapq_result == 1
    assert my_result == heapq_result

def test_negatives():
    nums = [-1, -2, -3, -4, -5]
    k = 2
    my_result = my_kth(nums, k)
    heapq_result = heapq_kth(nums, k)
    assert my_result == -2
    assert heapq_result == -2
    assert my_result == heapq_result

