import sys


def DFS(graph, startnode):
    notVisited, visited = list(), list()
    visited.append(startnode)

    while notVisited:
        node = notVisited.pop()
        if node not in visited:
            visited.append(node)
            notVisited.extend(graph[node])
    return visited


numOfComs = int(sys.stdin.readline())
numOfConect = int(sys.stdin.readline())


graph = dict()
for _ in range(numOfConect):
    x, y = map(int, sys.stdin.readline().strip().split(" "))
    if x not in graph.keys():
        graph[x] = set([y])
    else:
        graph[x].add(y)
    if y not in graph.keys():
        graph[y] = set([x])
    else:
        graph[y].add(x)



print(graph)
print(DFS(graph, 1))
