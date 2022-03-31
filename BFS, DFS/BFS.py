from collections import deque


def BFS_with_adj_list(graph, root):
    visited = list()
    queue = list()

    queue.append(root)

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue.extend(graph[n])
    return visited


graph_list = {
    1: set([3, 4]),
    2: set([3, 4, 5]),
    3: set([1, 5]),
    4: set([1]),
    5: set([2, 6]),
    6: set([3, 5]),
}
root_node = 1


print(BFS_with_adj_list(graph_list, root_node))
