# Uses python3
import sys


def get_change(m):
    """The goal in this problem is to find the minimum number of coins needed to change the input
     value (an integer) into coins with denominations 1, 5, and 10.
    Outputs the minimum number of coins with denominations 1, 5, 10 that changes m.
    """
    i = m % 10
    return (m // 10) + (i // 5) + i % 5

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
