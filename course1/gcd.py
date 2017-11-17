# python3
def gcd(x, y):
    '''Recursive function that calls itself until the modulo remainder of the
    two arguments equals zero, at which point it returns the first arg.
    '''
    return gcd(y, x % y) if y else abs(x)


if __name__ == '__main__':
    n = raw_input()
    # Split the input on spaces and cast as integers.
    x, y = map(int, n.split())
    print(gcd(x, y))
