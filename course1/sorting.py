# Uses python3
import sys
import random


def swap(a, x, y):
    # For the passed-in array, swap the elements at index x and y.
    tmp = a[x]
    a[x], a[y] = a[y], tmp


def partition3(a, l, r):
    # Implement Dijkstra 3-way partition.
    # Ref: https://algs4.cs.princeton.edu/lectures/23DemoPartitioning.pdf
    i = l
    lt = l
    gt = r
    piv = a[i]

    while i <= gt:
        if a[i] < piv:
            swap(a, lt, i)
            lt += 1
            i += 1
        elif a[i] > piv:
            swap(a, gt, i)
            gt -= 1
        else:
            i += 1
    return lt, gt


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m, n = partition3(a, l, r)
    #m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, n + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
