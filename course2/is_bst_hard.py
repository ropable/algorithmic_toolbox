#!/usr/bin/python3
import sys
import threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class Tree(object):

    def read(self):
        self.n = int(sys.stdin.readline())
        # Case: empty tree:
        if self.n == 0:
            self.key = [0]
            self.left = [-1]
            self.right = [-1]
        else:
            self.key = [0 for i in range(self.n)]
            self.left = [0 for i in range(self.n)]
            self.right = [0 for i in range(self.n)]
            for i in range(self.n):
                [a, b, c] = map(int, sys.stdin.readline().split())
                self.key[i] = a
                self.left[i] = b
                self.right[i] = c

    def in_order(self):
        self.result = []
        self.in_order_recurse(0)
        return self.result

    def in_order_recurse(self, root):
        if self.left[root] != -1:
            # If the left child is ever >= the parent, raise an Exception.
            if self.key[self.left[root]] >= self.key[root]:
                raise Exception('NOT A BST!')
            self.in_order_recurse(self.left[root])
        self.result.append(self.key[root])
        if self.right[root] != -1:
            self.in_order_recurse(self.right[root])

    def is_binary_search_tree(self):
        # If is_order returns a sorted result, then the tree is a balanced BST.
        try:
            in_order = self.in_order()
            in_order_sort = sorted(in_order)
            if in_order == in_order_sort:
                return True
            else:
                return False
        except:
            return False


def main():
    tree = Tree()
    tree.read()

    if tree.is_binary_search_tree():
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
