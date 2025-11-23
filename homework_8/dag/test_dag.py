from main import find_cycle, topological_sort, process_graph

def test_find_cycle_empty_graph():
    graph = {}
    result = find_cycle(graph)
    assert result is None

def test_find_cycle_simple_cycle():
    graph = {1: [2], 2: [3], 3: [1]}
    result = find_cycle(graph)
    expected_cycle = [1, 2, 3, 1]
    assert result == expected_cycle

def test_find_cycle_self_loop():
    graph = {1: [1], 2: [3], 3: []}
    result = find_cycle(graph)
    expected_cycle = [1, 1]
    assert result == expected_cycle

def test_find_cycle_no_cycle():
    graph = {1: [2], 2: [3], 3: []}
    result = find_cycle(graph)
    assert result is None

def test_topological_sort_empty_graph():
    graph = {}
    result = topological_sort(graph)
    assert result == []

def test_find_cycle_single_node():
    graph = {1: []}
    result = find_cycle(graph)
    assert result is None

def test_topological_sort():
    graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
    result = topological_sort(graph)
    assert 1 in result
    assert 2 in result
    assert 3 in result
    assert 4 in result
    assert result.index(1) < result.index(2)
    assert result.index(1) < result.index(3)
    assert result.index(2) < result.index(4)
    assert result.index(3) < result.index(4)

def test_topological_sort_many_components():
    graph = {1: [2], 2: [], 3: [4], 4: []}
    result = topological_sort(graph)
    assert len(result) == 4
    assert set(result) == {1, 2, 3, 4}
    assert result.index(1) < result.index(2)
    assert result.index(3) < result.index(4)

def test_topological_sort_linear_graph():
    graph = {1: [2], 2: [3], 3: [4], 4: []}
    result = topological_sort(graph)
    assert result == [1, 2, 3, 4]

def test_process_graph_empty():
    graph = {}
    result = process_graph(graph)
    assert result == []

def test_process_graph_single_node():
    graph = {1: []}
    result = process_graph(graph)
    assert result == [1]

def test_process_graph_with_cycle():
    graph = {1: [2], 2: [3], 3: [1]}
    result = process_graph(graph)
    expected_cycle = [1, 2, 3, 1]
    assert result == expected_cycle

def test_process_graph_without_cycle():
    graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
    result = process_graph(graph)
    assert len(result) == 4
    assert set(result) == {1, 2, 3, 4}

def test_process_graph_self_loop():
    graph = {1: [1], 2: []}
    result = process_graph(graph)
    assert result is not None
    assert result[0] == result[-1] 
