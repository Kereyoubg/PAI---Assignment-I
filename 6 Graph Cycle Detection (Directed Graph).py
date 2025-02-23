def dfs(node, graph, visited, recursion_stack):
    if recursion_stack[node]:
        return True

    if visited[node]:
        return False

    recursion_stack[node] = True
    visited[node] = True

    for neighbor in graph.get(node, []):
        if dfs(neighbor, graph, visited, recursion_stack):
            return True

    recursion_stack[node] = False
    return False


def has_cycle(graph):
    n = len(graph)
    visited = [False] * n
    recursion_stack = [False] * n

    # Try to detect a cycle starting from each node
    for node in range(n):
        if not visited[node]:
            if dfs(node, graph, visited, recursion_stack):
                return True

    return False


graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [0]
}
print(has_cycle(graph))
