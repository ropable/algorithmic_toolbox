# python3

import sys


NODES = {}  # Dict of graph nodes.


class GraphNodeUndirected(object):
    """A basic representation of an undirected graph node.
    """
    def __init__(self):
        self.visited = False
        self.pre_visit = None
        self.post_visit = None
        self.edges = []

    def __repr__(self):
        if self.visited:
            return 'Visited, edges: {}'.format(self.edges)
        else:
            return 'Unvisited, edges: {}'.format(self.edges)


def previsit(node, clock):
    node.pre_visit = clock
    #print('Set pre_visit to {}'.format(node.pre_visit))
    return clock + 1


def postvisit(node, clock):
    node.post_visit = clock
    return clock + 1


def explore(node, clock):
    if not NODES[node].visited:
        # For a given node, walk all of its edges and record the pre- and
        # post-visit clock.
        NODES[node].visited = True
        clock = previsit(NODES[node], clock)
        for w in NODES[node].edges:
            clock = explore(w, clock)
        clock = postvisit(NODES[node], clock)
    return clock


def reach(x, y):
    range1 = [i for i in range(NODES[x].pre_visit, NODES[x].post_visit + 1)]
    range2 = [i for i in range(NODES[y].pre_visit, NODES[y].post_visit + 1)]
    print(range1)
    print(range2)
    if range1[0] > range2[0] and range1[-1] < range2[-1]:
        return 1  # Nested (path exists)
    if range2[0] > range1[0] and range2[-1] < range1[-1]:
        return 1  # Nested (path exists)
    return 0  # Disjoint (no path)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    x, y = data[-2:]  # Last 2 values.
    for i in range(1, n + 1):
        NODES[i] = GraphNodeUndirected()

    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    for edge in edges:
        if edge[1] not in NODES[edge[0]].edges:
            NODES[edge[0]].edges.append(edge[1])
        if edge[0] not in NODES[edge[1]].edges:
            NODES[edge[1]].edges.append(edge[0])

    clock = 1
    for v in NODES.keys():
        clock = explore(v, clock)

    print(reach(x, y))
