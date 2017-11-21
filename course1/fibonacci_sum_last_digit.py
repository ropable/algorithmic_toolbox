# python3
import sys


def fibonacci_sum_naive(n):
    """Stupid example solution.
    """
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
    """Efficient algorithm to return F(n) via matrix multiplication.
    """
    if (n <= 1):
        return n
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2


def fib_sum_last_digit(n):
    """Returns the sum of Fibonacci numbers to n.
    Sn = Fn+2 - 1
    Ref: https://www.quora.com/What-is-the-sum-of-n-terms-of-a-Fibonacci-series
    """
    if n <= 1:
        return n

    n = (n + 2) % 60  # Use the characteristic of the last digit cycling every 60 numbers.
    return fib_matrix(n) - 1


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(str(fib_sum_last_digit(n))[-1:])
