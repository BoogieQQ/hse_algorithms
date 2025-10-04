from main import anagrams

def test_example():
    input_arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = anagrams(input_arr)
    
    result_sets = [set(group) for group in result]
    
    expected_groups = [
        {"eat", "tea", "ate"},
        {"tan", "nat"},
        {"bat"}
    ]
    
    assert len(result) == 3
    for expected_group in expected_groups:
        assert expected_group in result_sets

def test_empty_input():
    assert anagrams([]) == []

def test_single_element():
    assert anagrams(["eat"]) == [["eat"]]

def test_no_anagrams():
    input_arr = ["1", "2", "3"]
    result = anagrams(input_arr)
    
    assert len(result) == 3
    assert all([len(group) == 1 for group in result])

def test_all_same_anagrams():
    input_arr = ["123", "132", "312", "321"]
    result = anagrams(input_arr)
    
    assert len(result) == 1
    assert set(result[0]) == {"123", "132", "312", "321"}

def test_duplicate_strings():
    input_arr = ["123", "123", "123", "132", "312", "321"]
    result = anagrams(input_arr)
    
    assert len(result) == 1
    assert result[0] == ["123", "123", "123", "132", "312", "321"]

def test_whitespace():
    input_arr = ["1 2 3", "3 2 1", "123", "1 2 3"]
    result = anagrams(input_arr)
    
    result_sets = [set(group) for group in result]

    expected_groups = [
        {"1 2 3", "3 2 1", "1 2 3"},
        {"123"}
    ]
    
    for expected_group in expected_groups:
        assert expected_group in result_sets

def test_different_lengths():
    input_arr = ["1", "12", "21", "123", "1"]
    result = anagrams(input_arr)
    
    result_sets = [set(group) for group in result]
    
    expected_groups = [
        {"1", "1"},        
        {"12", "21"},      
        {"123"}            
    ]
    
    assert len(result) == 3
    for expected_group in expected_groups:
        assert expected_group in result_sets
