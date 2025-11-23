from main import Graph, dijkstra, get_dijkstra_path

def create_disconnected_graph():
    graph = Graph()
    graph.add_node(1, 2, 1)
    graph.add_node(3, 4, 1)
    return graph

def create_graph_from_wiki():
    graph = Graph()
    
    # Node 1 
    graph.add_node(1, 6, 14) 
    graph.add_node(1, 3, 9)
    graph.add_node(1, 2, 7)

    # Node 2   
    graph.add_node(2, 1, 7) 
    graph.add_node(2, 3, 10)
    graph.add_node(2, 4, 15)
    
    # Node 3
    graph.add_node(3, 6, 2)
    graph.add_node(3, 1, 9)
    graph.add_node(3, 2, 10)
    graph.add_node(3, 4, 11)
    
    # Node 4
    graph.add_node(4, 5, 6)
    graph.add_node(4, 3, 11)
    graph.add_node(4, 2, 15)

    # Node 5
    graph.add_node(5, 4, 6)
    graph.add_node(5, 6, 9)

    # Node 6
    graph.add_node(6, 1, 14) 
    graph.add_node(6, 3, 2)
    graph.add_node(6, 5, 9)
    
    return graph

def test_graph_initialization():
    graph = Graph()
    assert graph.nodes == {}

def test_add_node_creates_nodes():
    graph = Graph()
    graph.add_node(1, 2, 5)
    
    assert 1 in graph.nodes
    assert 2 in graph.nodes
    assert graph.nodes[1][2] == 5

def test_add_node_multiple_edges():
    graph = Graph()
    graph.add_node(1, 2, 1)
    graph.add_node(1, 3, 2)
    graph.add_node(1, 4, 3)
    
    assert len(graph.nodes[1]) == 3
    assert graph.nodes[1][2] == 1
    assert graph.nodes[1][3] == 2
    assert graph.nodes[1][4] == 3

def test_graph_getitem():
    graph = Graph()
    graph.add_node(1, 2, 5)
    
    assert graph[1] == {2: 5}
    assert graph[2] == {}
    assert graph[3] == {}

def test_basic():
    graph = create_graph_from_wiki()
    distances, path = dijkstra(graph, 1)
    
    expected_distances = {
        1: 0,
        2: 7,   
        3: 9,   
        4: 20,  
        5: 20,  
        6: 11
    }
    
    assert distances == expected_distances

def test_same_start_end():
    graph = create_graph_from_wiki()
    distances, path = dijkstra(graph, 1)
    
    path_to_self = get_dijkstra_path(path, 1)
    assert path_to_self == [1]
    assert distances[1] == 0

def test_path_1_to_4():
    graph = create_graph_from_wiki()
    distances, path = dijkstra(graph, 1)
    
    path_to_4 = get_dijkstra_path(path, 4)
    assert path_to_4 == [1, 3, 4]
    assert distances[4] == 20

def test_path_1_to_5():
    graph = create_graph_from_wiki()
    distances, path = dijkstra(graph, 1)
    
    path_to_5 = get_dijkstra_path(path, 5)
    assert path_to_5 == [1, 3, 6, 5]
    assert distances[5] == 20

def test_path_1_to_6():
    graph = create_graph_from_wiki()
    distances, path = dijkstra(graph, 1)
    
    path_to_6 = get_dijkstra_path(path, 6)
    assert path_to_6 == [1, 3, 6]
    assert distances[6] == 11

def test_from_different_start():
    graph = create_graph_from_wiki()
    distances, path = dijkstra(graph, 3)
    
    assert distances[3] == 0
    assert distances[1] == 9    
    assert distances[6] == 2   
    assert distances[2] == 10   
    assert distances[4] == 11  
    
    path_to_5 = get_dijkstra_path(path, 5)
    assert path_to_5 == [3, 6, 5]
    assert distances[5] == 11


def test_disconnected_graph():
    graph = create_disconnected_graph()
    distances, path = dijkstra(graph, 1)
    
    expected_distances = {
        1: 0,
        2: 1,
        3: float('inf'),
        4: float('inf')
    }
    
    assert distances == expected_distances

def test_no_path():
    graph = create_disconnected_graph()
    distances, path = dijkstra(graph, 1)
    
    path_to_3 = get_dijkstra_path(path, 3)
    assert path_to_3 == [3] 
    assert distances[3] == float('inf')
