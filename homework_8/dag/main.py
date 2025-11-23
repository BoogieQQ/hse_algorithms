def find_cycle(graph):
    visited = set()
    parent = {}
    recursion_stack = set()
    
    def dfs(start):
        stack = [start]
        visited.add(start)
        recursion_stack.add(start)
        parent[start] = None
        
        while stack:
            cur = stack[-1]
            
            found_unvisited = False
            for neighbour in graph.get(cur, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    recursion_stack.add(neighbour)
                    parent[neighbour] = cur
                    stack.append(neighbour)
                    found_unvisited = True
                    break
                
                elif neighbour in recursion_stack:
                    cycle = []
                    node = cur
                    while node != neighbour:
                        cycle.append(node)
                        node = parent[node]
                    
                    cycle.append(neighbour)
                    cycle.reverse()
                    cycle.append(neighbour)

                    return cycle
            
            if not found_unvisited:
                recursion_stack.remove(stack.pop())
        
        return None
    
    for node in graph:
        if node not in visited:
            cycle = dfs(node)
            if cycle:
                return cycle
    
    return None

def topological_sort(graph):
    visited = set()
    result = []
    
    def dfs(start):
        stack = [start]
        visited.add(start)
        
        while stack:
            cur = stack[-1]
            
            found_unvisited = False
            for neighbour in graph.get(cur, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)
                    found_unvisited = True
                    break
            
            if not found_unvisited:
                result.append(stack.pop())
    
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return result[::-1]

def process_graph(graph):
    cycle = find_cycle(graph)
    if cycle is not None:
        cycle = find_cycle(graph)
        print(f"Cycle found: {cycle}")
        return cycle
    else:
        topological_order = topological_sort(graph)
        print(f"No sycles. Topological order: {topological_order}")
        return topological_order