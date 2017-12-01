# Uses python3
import sys

"""
The algorithm begins by splitting the array in half repeatedly and calling itself
on each half.
When we get down to single elements, that single element is returned as the majority of
its (1-element) array. At every other level, it will get return values from its two
recursive calls.
The key to this algorithm is the fact that if there is a majority element in the
combined array, then that element must be the majority element in either the left
half of the array, or in the right half of the array. There are 4 scenarios.
a. Both return “no majority.” Then neither half of the array has a majority
element, and the combined array cannot have a majority element. Therefore,
the call returns “no majority.”
b. The right side is a majority, and the left isn’t. The only possible majority for
this level is with the value that formed a majority on the right half, therefore,
just compare every element in the combined array and count the number of
elements that are equal to this value. If it is a majority element then return
that element, else return “no majority.”
c. Same as above, but with the left returning a majority, and the right returning
“no majority.”
d. Both sub-calls return a majority element. Count the number of elements equal
to both of the candidates for majority element. If either is a majority element
in the combined array, then return it. Otherwise, return “no majority.”
The top level simply returns either a majority element or that no majority element
exists in the same way.
"""
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # Your code here
    return -1


def majority(data, tiebreaker=None):
    '''Return the majority element of sequence data, or
    tiebreaker - if exactly half of the elements in data are tiebreaker , or
    -1.
    '''
    n = len(data)
    if n == 0:
        return tiebreaker
    pairs = []
    if n % 2 == 1:
        tiebreaker = data[-1]
    for i in range(0, n-1, 2):
        if data[i] == data[i+1]:
            pairs.append(data[i])
    major = majority(pairs, tiebreaker)
    if major is None:
        return -1
    major_count = data.count(major)
    if 2 * major_count > n or (2 * major_count == n and major == tiebreaker ):
        return major
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
