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
    """Ref: https://stackoverflow.com/a/40930139/14508
    """
    return fib_matrix(to + 2) - fib_matrix(from_ + 1)


def fib_partial_sum_smarter(m, n):
    # Collect 60 Fibonnaci numbers:
    a = [0, 1]
    for i in range(2, 60):
        a.append(a[i-1] + a[i-2])

    # Simplify the input arguments as the last digit pattern repeats with a period of 60,
    # and the sum of 60 such consecutive numbers is 0 mod 10:
    m = m % 60
    n = n % 60
    # Make sure n is greater than m
    if n < m:
        n += 60

    su = 0
    for j in range(m, n + 1):  # Assume n index is inclusive
        su += a[j % 60]

    return su


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    #print(str(fib_partial_sum(from_, to))[-1:])
    print(fib_partial_sum_smarter(from_, to) % 10)
