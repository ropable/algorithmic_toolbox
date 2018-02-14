# python3

import sys


def reach(adj, x, y):
    # Determine if x can reach y by exploring all of the nodes that x can reach.
    visited = [False] * len(adj)  # List of all the edges, and whether they have been visited.
    return explore(adj, x, y, visited)


def explore(adj, x, y, visited):
    # Explore each edge pair.
    if x == y:  # Nodes are the same: we've reached y.
        return 1
    visited[x] = True
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:  # Recurse into each node of the pair.
            if explore(adj, adj[x][i], y, visited):
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]  # No. of vertices and edges.
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]  # u and v - is there a path between these?
    x, y = x - 1, y - 1  # They are zero-indexed.
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
