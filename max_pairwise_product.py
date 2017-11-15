#!/usr/bin/python
n = int(input())
a = [int(x) for x in input().split()]
result = 0
for i in range(0, len(a)):
    if a[i] * n > result:
        result = a[i] * n
print(result)
