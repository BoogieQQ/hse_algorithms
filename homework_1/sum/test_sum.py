from main import find_max

def test_examples():
    assert find_max("5 7 13 2 14") == 36
    assert find_max("3") == 0

def test_all_even_numbers():
    assert find_max("2 4 6 8 10") == 2 + 4 + 6 + 8 + 10
    assert find_max("56 32") == 56 + 32

def test_all_odd_numbers():
    assert find_max("1 3 5 7 9") == 3 + 5 + 7 + 9
    assert find_max("9 5 11") == 9 + 11

def test_permutations():
    assert find_max("1 2 3 5") == 2 + 3 + 5
    assert find_max("2 1 3 5") == 2 + 3 + 5
    assert find_max("2 3 1 5") == 2 + 3 + 5
    assert find_max("2 3 5 1") == 2 + 3 + 5


def test_duplicate_odd_numbers():
    assert find_max("3 3 2 4") == 3 + 3 + 2 + 4  
    assert find_max("1 1 1 1 1 1 1 1 2") == 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1+ 2 

def test_empty_string():
    assert find_max("") == 0

def test_single_even_number():
    assert find_max("2") == 2  
    assert find_max("0") == 0  
