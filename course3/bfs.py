# python3
import sys
from collections import deque


def distance(adj, s, t):
    # Instantiate the dist list from the slide.
    dist = [None] * len(adj)
    dist[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not dist[v]:  # Haven't yet recorded the path from the last node to this one.
                q.append(v)
                dist[v] = dist[u] + 1

    if dist[t]:  # If dist[t] is no longer None, we've found a path.
        return dist[t]

    return -1


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
