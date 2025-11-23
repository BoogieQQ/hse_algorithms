import heapq

class Graph:
    def __init__(self):
        self.nodes = {}

    def __getitem__(self, key):
        return self.nodes[key] if key in self.nodes else {}

    def add_node(self, node_from, node_to, weight):
        if node_from not in self.nodes:
            self.nodes[node_from] = {}
        
        if node_to not in self.nodes:
            self.nodes[node_to] = {}

        self.nodes[node_from][node_to] = weight
    

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    path = {node: None for node in graph.nodes}
    heap = [(0, start)]

    while heap:
        distance, node = heapq.heappop(heap)

        if distance > distances[node]:
            continue

        for next_node, weight in graph[node].items():
            cur_distance = distance + weight

            if cur_distance < distances[next_node]:
                path[next_node] = node
                distances[next_node] = cur_distance
                heapq.heappush(heap, (cur_distance, next_node))

    return distances, path

def get_dijkstra_path(previous, target):
    res = []
    current = target
    
    while current is not None:
        res.append(current)
        current = previous[current]
    
    res.reverse()
    return res



