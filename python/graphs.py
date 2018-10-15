from collections import deque

def dfs_recursive(graph, start, seen):
    seen[start] = True
    print("visiting node " + str(start))
    for neighbor in graph[start]:
        if not seen[neighbor]:
            dfs_recursive(graph, neighbor, seen)

def dfs_iterative(graph, start, seen):
    seen[start] = True
    print("visiting node " + str(start))
    to_visit = deque()
    to_visit = [start]
    while to_visit:
        node = to_visit.pop()
        for neighbor in graph[node]:
            if not seen[neighbor]:
                seen[neighbor] = True
                print("visiting node " + str(neighbor))
                to_visit.append(neighbor)

def bfs(graph, start=0):
    to_visit = deque()  # queue of nodes to visit
    # init array for distances between start and each nodes of the graph
    dist = [float('inf')] * len(graph)
    # init array for predecesor of each node on the path: start -> node
    pred = [None] * len(graph)
    dist[start] = 0  # distance from start to start = 0
    to_visit.appendleft(start)
    while to_visit:  # empty queue returns false
        node = to_visit.pop()
        for neighbor in graph[node]:
            # if distance not evaluated yet i.e distance == infinity
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[node] + 1
                pred[neighbor] = node
                to_visit.appendleft(neighbor)
    return dist, pred

def main():
    print("Graph based algorithms")
    graph = { 0:[1], 1:[2], 2:[1] }
    bfs(graph, 0)
    print('bfs done')
    # dfs_recursive(graph, 0, [None] * len(graph))
    dfs_iterative(graph, 0, [None] * len(graph))


if __name__ == "__main__":
    main()
