# python3
import sys


def get_fibonacci_huge_naive(n, m):
    '''The slow example solution.
    '''
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def fib_huge(n, m):
    '''Recycled matrix multiplication solution, modulo m at the required steps.
    Ref: https://en.wikipedia.org/wiki/Pisano_period
    '''
    if (n <= 1):
        return n
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = (v2 * v2) % m
        v1, v2, v3 = (v1 * v1 + calc) % m, ((v1 + v3) * v2) % m, (calc + v3 * v3) % m
        if rec == '1':
            v1, v2, v3 = (v1 + v2) % m, v1, v2
    return v2

if __name__ == '__main__':
    n = sys.stdin.read()
    n, m = map(int, n.split())
    print(fib_huge(n, m))
