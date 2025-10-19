from main import permutations

def test_example1():
    result = permutations([1, 2, 3])
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    assert result == expected

def test_example2():
    result = permutations([0,1])
    expected = [[0,1],[1,0]]
    assert result == expected

def test_example3():
    result = permutations([1])
    expected = [[1]]
    assert result == expected

def test_empty_list():
    result = permutations([])
    expected = [[]]
    assert result == expected

def test_with_duplicate_elements():
    result = permutations([1, 1])
    expected = [[1, 1], [1, 1]]
    assert result == expected

def test_with_strings():
    result = permutations(['a', 'b'])
    expected = [['a', 'b'], ['b', 'a']]
    assert sorted(result) == sorted(expected)


def test_with_mixed_types():
    result = permutations([1, 'a'])
    expected = [[1, 'a'], ['a', 1]]
    assert result == expected
