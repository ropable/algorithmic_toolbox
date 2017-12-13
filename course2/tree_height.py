# python3
import sys


class Node(object):
    """A generic node class with some helper methods.
    """
    def __init__(self, name, parent=None, children=None):
        self.name = name
        self.parent = parent
        self.children = []
        if children:
            for child in children:
                self.add_child(child)

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return 'Node {} (parent: {})'.format(self.name, self.parent)

    def add_child(self, node):
        self.children.append(node)

    def is_leaf(self):
        if self.children:
            return False
        return True

    def is_root(self):
        if self.parent:
            return False
        return True

    def path_to_root(self):
        """Follow parent nodes back to the root node.
        """
        path = [self]
        if self.is_root():
            return path
        root = False
        current = self.parent

        while not root:
            path.append(current)
            if current.is_root():
                root = True
            else:
                current = current.parent

        return path


def allocate_nodes(parents):
    """Construct a tree from the input list of parent nodes.
    """
    tree = {i: Node(i) for i, j in enumerate(parents)}
    root_node = None

    for i, parent in enumerate(parents):
        if parent >= 0:
            # Set the parent for that node.
            tree[i].parent = tree[parent]
            # Add the current node as a child of the parent.
            tree[parent].add_child(tree[i])
        else:
            root_node = tree[i]

    return tree, root_node


def calculate_tree_height(tree):
    """Iterate through a tree and calculate the height.
    """
    max_height = 0
    for i in tree.values():
        if i.is_leaf():
            path = i.path_to_root()
            if len(path) > max_height:
                max_height = len(path)

    return max_height


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    parents = list(map(int, sys.stdin.readline().split()))
    tree, root_node = allocate_nodes(parents)
    print(calculate_tree_height(tree))
