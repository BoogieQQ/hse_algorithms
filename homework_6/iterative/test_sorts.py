from itertools import permutations
from main import timed_quicksort, timed_mergesort


def test_sort_empty():
    assert timed_quicksort([])['result'] == []
    assert timed_mergesort([])['result'] == []

def test_sort_one_element():
    assert timed_quicksort([0])['result'] == [0]
    assert timed_mergesort([0])['result'] == [0]

def test_sort_three_elements():
    tests = [list(test) for test in permutations([1,2,3])]
    for test in tests:
        assert timed_quicksort(test)['result'] == [1,2,3]
        assert timed_mergesort(test)['result'] == [1,2,3]

def test_sort_four_elements():
    tests = [list(test) for test in permutations([1,2,3,4])]
    for test in tests:
        assert timed_quicksort(test)['result'] == [1,2,3,4]
        assert timed_mergesort(test)['result'] == [1,2,3,4]

def test_quicksort_worst_case_vs_mergesort():
    worst_case = list(range(1000))
    
    quick_result = timed_quicksort(worst_case)
    merge_result = timed_mergesort(worst_case)
    
    assert quick_result['time'] > merge_result['time'] * 1.5

def test_reverse_sorted_performance():
    reverse_sorted = list(range(1000, 0, -1))
    
    quick_result = timed_quicksort(reverse_sorted)
    merge_result = timed_mergesort(reverse_sorted)
    
    assert quick_result['time'] > merge_result['time'] * 1.5

def test_sort_random():
    import random
    large_list = [random.randint(1, 1000) for _ in range(1000)]
    
    quick_result = timed_quicksort(large_list.copy())
    merge_result = timed_mergesort(large_list.copy())
    
    expected = sorted(large_list)
    assert quick_result['result'] == sorted(expected)
    assert merge_result['result'] == sorted(expected)


def test_duplicate_elements():
    duplicate_list = [1,2,3,2,2,2,2,3,1,3,2,2,2,3,1,3]
    
    quick_result = timed_quicksort(duplicate_list.copy())
    merge_result = timed_mergesort(duplicate_list.copy())
    
    expected = sorted(duplicate_list)
    assert quick_result['result'] == expected
    assert merge_result['result'] == expected


def test_negative_numbers():
    test_list = [0,-1,1,-2,2,-3,3,-4,4,-5,5]
    
    quick_result = timed_quicksort(test_list.copy())
    merge_result = timed_mergesort(test_list.copy())
    
    expected = sorted(test_list)
    assert quick_result['result'] == expected
    assert merge_result['result'] == expected

def test_strings():
    test_list = ['d','a','b','c']
    
    quick_result = timed_quicksort(test_list.copy())
    merge_result = timed_mergesort(test_list.copy())
    
    expected = ['a', 'b', 'c', 'd']
    assert quick_result['result'] == expected
    assert merge_result['result'] == expected
