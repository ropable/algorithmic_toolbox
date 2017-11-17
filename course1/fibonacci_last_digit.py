# python3
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


if __name__ == '__main__':
    n = int(input())
    print(str(fib_matrix(n))[-1:])
