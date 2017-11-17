# python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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


def fib_partial_sum(from_, to):
    total = 0

    for i in range(from_, to + 1):
        total += fib_matrix(i)

    return total


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(str(fib_partial_sum(from_, to))[-1:])
