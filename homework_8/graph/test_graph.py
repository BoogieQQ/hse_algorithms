from main import find_components

def test_empty_graph():
    graph = {}
    result = find_components(graph)
    assert result == []

def test_single_node():
    graph = {1: []}
    result = find_components(graph)
    assert result == [[1]]

def test_single_node_with_self_loop():
    graph = {
        1: [1]
    }
    result = find_components(graph)
    assert result == [[1]]

def test_single_component():
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    result = find_components(graph)

    assert len(result) == 1
    assert set(result[0]) == {1, 2, 3}

def test_disconnected_components():
    graph = {
        1: [],
        2: [],
        3: []
    }
    result = find_components(graph)
    assert len(result) == 3
    assert sorted(result) == [[1], [2], [3]]

def test_linear_graph():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2],
    }
    result = find_components(graph)
    assert len(result) == 1
    assert set(result[0]) == {1, 2, 3}

def test_cyclic_graph():
    graph = {
        1: [2],
        2: [3],
        3: [1] 
    }
    result = find_components(graph)
    assert len(result) == 1
    assert set(result[0]) == {1, 2, 3}

def test_many_cyclic_graph():
    graph = {
        # 1
        1: [2],
        2: [3],
        3: [1],
        
        # 2
        4: [5],
        5: [6],
        6: [4],

        # 3
        7: [8],
        8: [9],
        9: [7]  
    }
    result = find_components(graph)
    components_sets = [set(comp) for comp in result]

    assert len(result) == 3
    assert {1, 2, 3} in components_sets
    assert {4, 5, 6} in components_sets
    assert {7, 8, 9} in components_sets

def test_node_with_no_edges():
    graph = {
        1: [2],
        2: [1],
        3: [], 
        4: [5],
        5: [4]
    }
    result = find_components(graph)
    components_sets = [set(comp) for comp in result]

    assert len(result) == 3
    assert {1, 2} in components_sets
    assert {3}    in components_sets
    assert {4, 5} in components_sets

def test_duplicate_edges():
    graph = {
        1: [2, 2, 3],
        2: [1, 1], 
        3: [1]
    }
    result = find_components(graph)
    assert len(result) == 1

def test_self_loops():
    graph = {
        1: [1, 2],
        2: [1],
        3: [3]
    }
    result = find_components(graph)
    assert len(result) == 2