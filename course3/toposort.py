# python3
import sys


class Digraph(object):

    def __init__(self, v):
        self.adj = [[] for i in range(v)]  # Adjacency list.

    def __repr__(self):
        return '{}'.format(self.adj)

    def add_edge(self, v, w):
        # Add a directed edge from v to w (if not already present).
        if w not in self.adj[v]:
            self.adj[v].append(w)

    def edge_count(self):
        count = 0
        for i in self.adj:
            count += len(i)
        return count

    def print_edges(self):
        for v, i in enumerate(self.adj):
            if i:
                for e in i:
                    print('{} -> {}'.format(v, e))
            else:
                print('{}'.format(v))


def dfs(graph, v, visited, order):
    visited[v] = True
    for w in graph.adj[v]:
        if not visited[w]:
            dfs(graph, w, visited, order)
    order.append(v)


def depth_first_order(graph):
    order = []
    visited = [False] * len(graph.adj)
    for v in range(len(graph.adj)):
        if not visited[v]:
            dfs(graph, v, visited, order)
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    g = Digraph(n)
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        g.add_edge(a - 1, b - 1)

    topo_order = depth_first_order(g)
    topo_order.reverse()  # Topological order is reverse DFS order.
    for x in topo_order:
        print(x + 1, end=' ')
