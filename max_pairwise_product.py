# python3
"""Input:
n
a b c ... z
"""
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)  # Input validation (n is a count of the input integers)
result = 0

# Inefficient solution:
"""
for i in range(0, n):
    for j in range(i+1, n):
        if a[i]*a[j] > result:
            result = a[i]*a[j]
"""

# Efficient solution:
a.sort(reverse=True)
result = a[0] * a[1]

print(result)
