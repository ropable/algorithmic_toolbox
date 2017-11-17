# python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fib_matrix(n):
    if (n <= 1):
        return n
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2


def fib_sum(n):
    """Returns the sum of Fibonacci number to n.
    """
    if n <= 1:
        return n

    total = 1
    for i in range(2, n + 1):
        total += fib_matrix(i)

    return total


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(str(fib_sum(n))[-1:])
