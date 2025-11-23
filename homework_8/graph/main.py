def find_components(graph):
    visited = set()
    components = []
    def dfs(start):
        stack = [start]
        visited.add(start)
        component = []

        while stack:
            cur = stack.pop()
            component.append(cur)
            for neighbour in graph.get(cur, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)
        
        return component
        
    for neighbour in graph:
        if neighbour not in visited:
            components.append(dfs(neighbour))

    return components