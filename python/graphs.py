from collections import deque


def bfs(graph, start=0):
    to_visit = deque()  # queue of nodes to visit
    # init array for distances between start and each nodes of the graph: all infinity
    dist = [float('inf')] * len(graph)
    # init array for predecesor of each node on the path: start -> node
    prec = [None] * len(graph)
    dist[start] = 0  # distance from start to start = 0
    to_visit.appendleft(start)
    while to_visit:  # empty queue returns false
        node = to_visit.pop()
        for neighbor in graph[node]:
            # if distance not evaluated yet i.e distance == infinity
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[node] + 1
                prec[neighbor] = node
                to_visit.appendleft(neighbor)
    return dist, prec


def main():
    print("Graph based algorithms")


if __name__ == "__main__":
    main()
