from main import quickselect

def test_example1():
    assert quickselect([3,2,1,5,6,4], 2) == 5

def test_example2():
    assert quickselect([3,2,3,1,2,4,5,5,6], 4) == 4

def test_empty():
    assert quickselect([], 1) is None

def test_quickselect_basic():
    test = [3, 1, 4, 2, 5]
    test_sorted = sorted(test)
    for i in range(1, len(test)+1):
        assert quickselect(test.copy(), i) == test_sorted[-i]


def test_quickselect_single_element():
    test = [0]
    assert quickselect(test, 1) == 0


def test_quickselect_duplicates():
    test = [3, 2, 2, 1, 3, 1]
    test_sorted = sorted(test)
    for i in range(1, len(test)+1):
        assert quickselect(test.copy(), i) == test_sorted[-i]

def test_quickselect_negative_numbers():
    test = [-i for i in range(1, 10)]
    for i in range(1, len(test)+1):
        assert quickselect(test.copy(), i) == test[i-1]

def test_quickselect_mixed_numbers():
    test = [-2,-1,0,1,2]
    for i in range(1, len(test)+1):
        assert quickselect(test.copy(), i) == test[-i]


def test_quickselect_all_same_elements():
    test = [0,0,0,0,0,0]
    for i in range(1, len(test)+1):
        assert quickselect(test.copy(), i) == 0


def test_quickselect_edge_cases():
    test = [1, 2, 3]
    assert quickselect(test.copy(), 0) is None    
    assert quickselect(test.copy(), 4) is None    
    assert quickselect(test.copy(), -1) is None   
