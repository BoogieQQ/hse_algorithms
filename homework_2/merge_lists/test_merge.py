from main import merge_two_lists_with_dummy, merge_two_lists_without_dummy

def test_merge_basic_case():
    result1 = merge_two_lists_with_dummy([1, 2, 4], [1, 3, 4])
    result2 = merge_two_lists_without_dummy([1, 2, 4], [1, 3, 4])
    
    assert result1.get_elems() == [1, 1, 2, 3, 4, 4]
    assert result2.get_elems() == [1, 1, 2, 3, 4, 4]
    assert len(result1) == 6
    assert len(result2) == 6

def test_merge_first_list_empty():
    result1 = merge_two_lists_with_dummy([], [1, 3, 4])
    result2 = merge_two_lists_without_dummy([], [1, 3, 4])
    
    assert result1.get_elems() == [1, 3, 4]
    assert result2.get_elems() == [1, 3, 4]
    assert len(result1) == 3
    assert len(result2) == 3

def test_merge_second_list_empty():
    result1 = merge_two_lists_with_dummy([1, 2, 4], [])
    result2 = merge_two_lists_without_dummy([1, 2, 4], [])
    
    assert result1.get_elems() == [1, 2, 4]
    assert result2.get_elems() == [1, 2, 4]
    assert len(result1) == 3
    assert len(result2) == 3

def test_merge_both_lists_empty():
    result1 = merge_two_lists_with_dummy([], [])
    result2 = merge_two_lists_without_dummy([], [])
    
    assert result1.get_elems() == []
    assert result2.get_elems() == []
    assert len(result1) == 0
    assert len(result2) == 0
    assert result1.is_empty() == True
    assert result2.is_empty() == True

def test_merge_single_elements():
    result1 = merge_two_lists_with_dummy([1], [2])
    result2 = merge_two_lists_without_dummy([1], [2])
    
    assert result1.get_elems() == [1, 2]
    assert result2.get_elems() == [1, 2]
    assert len(result1) == 2
    assert len(result2) == 2

def test_merge_duplicate_elements():
    result1 = merge_two_lists_with_dummy([1, 1, 3], [1, 2, 2])
    result2 = merge_two_lists_without_dummy([1, 1, 3], [1, 2, 2])
    
    assert result1.get_elems() == [1, 1, 1, 2, 2, 3]
    assert result2.get_elems() == [1, 1, 1, 2, 2, 3]
    assert len(result1) == 6
    assert len(result2) == 6

def test_merge_different_lengths1():
    result1 = merge_two_lists_with_dummy([1, 2, 5], [3, 4, 8, 15])
    result2 = merge_two_lists_without_dummy([1, 2, 5], [3, 4, 8, 15])
    
    assert result1.get_elems() == [1, 2, 3, 4, 5, 8, 15]
    assert result2.get_elems() == [1, 2, 3, 4, 5, 8, 15]
    assert len(result1) == 7
    assert len(result2) == 7

def test_merge_different_lengths2():
    result1 = merge_two_lists_with_dummy([1, 2, 5, 15], [3, 4, 8])
    result2 = merge_two_lists_without_dummy([1, 2, 5, 15], [3, 4, 8])
    
    assert result1.get_elems() == [1, 2, 3, 4, 5, 8, 15]
    assert result2.get_elems() == [1, 2, 3, 4, 5, 8, 15]
    assert len(result1) == 7
    assert len(result2) == 7

def test_merge_negative_numbers():
    result1 = merge_two_lists_with_dummy([-5, -1, 0], [-3, -2, 1])
    result2 = merge_two_lists_without_dummy([-5, -1, 0], [-3, -2, 1])
    
    assert result1.get_elems() == [-5, -3, -2, -1, 0, 1]
    assert result2.get_elems() == [-5, -3, -2, -1, 0, 1]

def test_merge_identical_lists():
    result1 = merge_two_lists_with_dummy([1, 2, 3], [1, 2, 3])
    result2 = merge_two_lists_without_dummy([1, 2, 3], [1, 2, 3])
    
    assert result1.get_elems() == [1, 1, 2, 2, 3, 3]
    assert result2.get_elems() == [1, 1, 2, 2, 3, 3]

def test_merge_head_and_tail_correct():
    result1 = merge_two_lists_with_dummy([1, 3], [2, 4])
    result2 = merge_two_lists_without_dummy([1, 3], [2, 4])
    
    assert result1.head.data == 1
    assert result1.tail.data == 4
    assert result2.head.data == 1
    assert result2.tail.data == 4
