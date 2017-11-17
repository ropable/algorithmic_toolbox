# python3
import sys


def fib_slow(n):
    '''Dumb (slow) example solution.
    '''
    if (n <= 1):
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)


def fib_countup(n):
    '''Less-dumb 'count up as you go' solution.
    '''
    if (n <= 1):
        return n
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x


def fib_memoize(n, saved={0: 0, 1: 1}):
    '''Use memoization to speed things up.
    '''
    if (n <= 1):
        return n
    if n not in saved:
        saved[n] = fib_memoize(n-1, saved) + fib_memoize(n-2, saved)
    return saved[n]


def fib_matrix(n):
    '''Use matrix multiplication to solve it.
    Ref: https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
    '''
    if (n <= 1):
        return n
    v1, v2, v3 = 1, 1, 0  # Initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # Raise it to the nth power
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(fib_matrix(n))
