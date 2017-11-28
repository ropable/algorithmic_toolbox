# Uses python3
import sys


def optimal_summands(n):
    # Short-circuit.
    if n <= 2:
        return [n]

    # Safe move: take 1 as the first summand.
    summands, l, k = [], 1, n

    # Progressively reduce n by greater unique summands.
    while k > 0:
        if k <= 2 * l:
            summands.append(k)
            k -= k
        else:
            summands.append(l)
            k -= l
        l += 1

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
