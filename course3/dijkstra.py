# python3

from functools import total_ordering
import sys
#from math import inf  # Coursera uses < Python 3.5, grr
import queue


@total_ordering
class Node(object):
    """A trivial class to represent nodes as a distance from some initial node.
    Comparison is performed by distance.
    """
    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __lt__(self, other):
        return self.distance < other.distance


def distance(adj, cost, s, t):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist = [float('inf')] * len(adj)
    dist[s] = 0

    while not pq.empty():
        u = pq.get().index
        for dest in adj[u]:  # Examine all other nodes adjacent to u
            v = adj[u].index(dest)
            if dist[dest] > dist[u] + cost[u][v]:
                dist[dest] = dist[u] + cost[u][v]
                pq.put(Node(dest, dist[dest]))
    if dist[t] == float('inf'):
        return -1
    return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]  # Node adjacency.
    cost = [[] for _ in range(n)]  # Node distance (corresponds to adjacency).
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1  # s: initial node, t: destination
    print(distance(adj, cost, s, t))
