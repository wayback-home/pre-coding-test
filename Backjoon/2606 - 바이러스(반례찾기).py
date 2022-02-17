import sys

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


def find_graph(graph):
    visited = list()
    visited.append(int(1))

    i = 1
    while i in graph.keys():
        if i in visited:
            visited.extend(graph.get(i))
            i += 1
        else:
            i += 1

    setVisited = set(visited)
    visited = list(setVisited)

    return len(visited) - 1


print(find_graph(graph))
