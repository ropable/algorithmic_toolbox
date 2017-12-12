# python3
import sys


class TreeHeight:
    def __init__(self, parents):
        self._parents = parents
        self._n = len(parents)
        self._max_height = None
        self._heights = [None] * self._n

    def max_height(self):
        if self._max_height is not None:
            return self._max_height
        for i, parent in enumerate(self._parents):
            parent_stack = []
            while parent != -1 and self._heights[i] is None:
                parent_stack.append(i)
                i, parent = parent, self._parents[parent]
            if parent == -1:
                height = 1
            else:
                height = self._heights[i]
            while parent_stack:
                self._heights[parent_stack.pop()] = height
                height += 1
            if not self._max_height or self._max_height < height:
                self._max_height = height
        return self._max_height


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    parents = list(map(int, sys.stdin.readline().split()))
    tree = TreeHeight(parents)
    print(tree.max_height())
