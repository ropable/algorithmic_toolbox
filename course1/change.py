# Uses python3
import sys


def get_change(m):
    """The goal in this problem is to find the minimum number of coins needed to change the input
     value (an integer) into coins with denominations 1, 5, and 10.
    Outputs the minimum number of coins with denominations 1, 5, 10 that changes m.
    """
    return (m // 10) + ((m % 10) // 5) + (m % 10) % 5

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
