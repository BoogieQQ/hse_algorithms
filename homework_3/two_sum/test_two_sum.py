from main import two_sum


def test_example1():
    assert two_sum([1, 3, 4, 10], 7) == (1, 2)

def test_example2():
    assert two_sum([5, 5, 1, 4], 10) == (0, 1)

def test_negative_numbers():
    assert two_sum([-3, 0, 3, 1], 0) == (0, 2)

def test_duplicate_numbers():
    assert two_sum([0, 0], 0) == (0, 1)

# Не нужно, так как гарантируется уникальность, но пусть будет
def test_many_pairs():
    assert two_sum([0, 0, -1, 1, -2, 2], 0) == (0, 1)
    assert two_sum([0, 0, 0, 0, 0, 0], 0) == (0, 1)

def test_empty():
    assert two_sum([], 100) is None

def test_not_found():
    assert two_sum([1,2,3,4,5], 100) is None

