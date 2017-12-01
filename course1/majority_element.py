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

Ref: http://www.chegg.com/homework-help/array-1-n-said-majority-element-half-entries-given-array-ta-chapter-2-problem-23-solution-9780077388492-exc
"""

def majority(a):
    # Initially check for a single-element array, and return that element
    # (always majority).
    if len(a) == 1:
        return a[0]
    # Next, find the middle of the array.
    mid = len(a) // 2
    # Recursively call this function on the left and right halves of the array.
    l_elem = majority(a[:mid])
    r_elem = majority(a[mid:])
    # These two calls will be one of three cases:
    # 1. Both return -1 (neither majority)
    # 2. Both return a value as the majority
    # 3. One returns a value as the majority, one does not

    # If both halves return the same value, pass that up as the majority value.
    if l_elem == r_elem:
        return l_elem
    # Check the count of the majority elements (if returned).
    # If either makes up more than half the passed-in array, pass that element
    # up again.
    if l_elem != -1:
        l_count = a.count(l_elem)
        if l_count > mid:
            return l_elem
    if r_elem != -1:
        r_count = a.count(r_elem)
        if r_count > mid:
            return r_elem

    # If all else fails, return -1 (no majority element).
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if majority(a) != -1:
        print(1)
    else:
        print(0)
