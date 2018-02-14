# python3
import sys


def number_of_components(adj):
    result = 0
    visited = [False] * len(adj)
    for i in range(len(adj)):
        if not visited[i]:
            explore(adj, i, visited)
            result += 1
    return result


def explore(adj, x, visited):
    # Fully explore each edge pair.
    visited[x] = True
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:  # Recurse into each node of the pair.
            explore(adj, adj[x][i], visited)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
