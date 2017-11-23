#Uses python3

import sys


def max_dot_product(a, b):
    # Safe move: match the highest value with the highest clicks
    return sum([x * y for x, y in zip(sorted(a, reverse=True), sorted(b, reverse=True))])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
