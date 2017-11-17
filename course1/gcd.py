# python3

def gcd(x, y):
    return gcd(y, x % y) if y else abs(x)


n = input()
x, y = map(int, n.split())
print(gcd(x, y))
