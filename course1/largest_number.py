#Uses python3

import sys
import random


def stress_test():
    """Generate a list of random integers that meet the problem constraints.
    """
    n = random.randint(1, 100)
    s = []
    for i in range(n):
        s.append(random.randint(1, 10**3))
    return s


def isGreater(m, n):
    """Implement the solution straight from the problem document.
    """
    if not n:  # n might be None.
        return True
    # Consider both combinations: mn and nm.
    m, n = str(m), str(n)
    m_first = int(m + n)
    n_first = int(n + m)
    if m_first > n_first:
        return True
    return False


def largest_number(a):
    answer = []
    while a:
        maxDigit = None
        for digit in a:
            if isGreater(digit, maxDigit):
                maxDigit = digit
        answer.append(maxDigit)
        a.remove(maxDigit)

    return int(''.join(map(str, answer)))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
