# python3
import sys


def lcm_naive(a, b):
    '''Dumb (slow) example solution.
    '''
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b


def gcd(x, y):
    '''Recycled GCD solution.
    '''
    return gcd(y, x % y) if y else abs(x)


def lcm(a, b):
    '''Return the product of the two ints, divided by their GCD.
    Use floor (not floating point) division.
    Ref: https://stackoverflow.com/a/183870/14508
    '''
    return a * b // gcd(a, b)


if __name__ == '__main__':
    n = sys.stdin.read()
    x, y = map(int, n.split())
    print(lcm(x, y))
