# python3

import sys


def explore(v, visited, rec_stack, adj):
    # Mark the current node as visited and add it to the recursion stack.
    visited[v] = True
    rec_stack[v] = True

    # Recur for all neighbours - if any neighbour is visited and in rec_stack,
    # then the graph is cyclic.
    for i in adj[v]:
        if visited[i] is False:  # Recurse into each node of the list of targets.
            if explore(i, visited, rec_stack, adj) is True:
                return True
        elif rec_stack[i] is True:
            return True

    rec_stack[v] = False
    return False


def acyclic(adj):
    """For this list of directed edges, perform a DFS for each node/edge.
    If any node returns a path to itself, return 1.
    Otherwise return 0.
    """
    visited = [False] * len(adj)
    rec_stack = [False] * len(adj)
    for i in range(len(adj)):
        if visited[i] is False:
            if explore(i, visited, rec_stack, adj) is True:
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
