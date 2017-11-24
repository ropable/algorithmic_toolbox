# python3
import sys


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


"""
But wait - the last digit of every number in the Fibonacci sequence repeats every
60th number! Irrespective of how large n is, its last digit is going to have appeared
somewhere within the sequence.
Ref: https://www.goldennumber.net/fibonacci-60-repeating-pattern/

* Sum of nth Fibonacci series = F(n+2) -1
* Then pisano period of modulo 10 = let n+2 mod (60) = m then find F(m) mod(10)-1
"""

if __name__ == '__main__':
    n = int(sys.stdin.read())
    m = (n + 2) % 60
    fm = (fib_matrix(m)) % 10
    print(fm - 1)
