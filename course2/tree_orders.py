# python3

import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders(object):
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        self.inOrder_rec(0)
        return self.result

    def inOrder_rec(self, root):
        if self.left[root] != -1:
            self.inOrder_rec(self.left[root])
        self.result.append(self.key[root])
        if self.right[root] != -1:
            self.inOrder_rec(self.right[root])

    def preOrder(self):
        self.result = []
        self.preOrder_rec(0)
        return self.result

    def preOrder_rec(self, root):
        self.result.append(self.key[root])
        if self.left[root] != -1:
            self.preOrder_rec(self.left[root])
        if self.right[root] != -1:
            self.preOrder_rec(self.right[root])

    def postOrder(self):
        self.result = []
        self.postOrder_rec(0)
        return self.result

    def postOrder_rec(self, root):
        #print('Passed in {}'.format(root))
        #print('Node {}'.format(self.key[root]))
        #print('Left = {}'.format(self.left[root]))
        #print('Right = {}'.format(self.right[root]))
        if self.left[root] != -1:
            self.postOrder_rec(self.left[root])
        if self.right[root] != -1:
            self.postOrder_rec(self.right[root])
        self.result.append(self.key[root])


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
