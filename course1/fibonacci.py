# python3
def calc_fib(n):
    '''Dumb (slow) example solution.
    '''
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_countup(n):
    '''Less-dumb 'count up as you go' solution.
    '''
    if (n <= 1):
        return n

    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

n = int(input())
print(calc_fib_countup(n))
