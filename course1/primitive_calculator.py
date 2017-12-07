# Uses python3
import sys


D = {}


def calc(n):
    """Return a tuple of (min steps, previous number)
    Memoize the results in D.
    """
    if n == 1:
        return (1, 0)
    if D.get(n):  # Save some time by returning any existing calculated result.
        return D[n]

    # Call this function to return the number of steps for n - 1 (always applicable).
    # ans is a tuple (steps+1, previous n used)
    ans = (calc(n-1)[0] + 1, n - 1)

    # Call this function to return the number of steps for n / 2 (if applicable).
    if n % 2 == 0:
        ans2 = calc(n // 2)
        if ans[0] > ans2[0]:
            ans = (ans2[0] + 1, n // 2)

    # Call this function to return the number of steps for n / 3 (if applicable).
    if n % 3 == 0:
        ans2 = calc(n // 3)
        if ans[0] > ans2[0]:
            ans = (ans2[0] + 1, n // 3)

    D[n] = ans
    return ans


def sequence(n):
    """Repeatedly call calc() from n until n = 1
    """
    for i in range(1, n):
        calc(i)[0]
    ans = []
    while calc(n)[1] != 0:
        ans.append(n)
        n = calc(n)[1]
    ans.append(1)
    ans.reverse()
    return ans


def optimal_sequence(n):
    """Return the optimal sequence for our primitive calculator to return n.
    Operations are: +1, *2 or *3.
    We're implementing a variation of the change problem (DPChange algo).
    """
    sequence = []
    # First, initialise an array of length n + 1 to store the optimal path
    # to each intervening value.
    steps_array = [0] * (n + 1)
    steps_array[1] = 1  # Only one possibility.

    for idx in range(2, len(steps_array)):
        # idx is the value that we need to calculate the optimal no of steps to reach.
        # Find all the candidate previous paths ().
        prev_steps = [idx - 1]  # idx - 1 is always a path option.
        # If idx is divisible by 2 or 3, consider those as paths.
        if idx % 2 == 0:
            prev_steps.append(idx // 2)
        if idx % 3 == 0:
            prev_steps.append(idx // 3)
        #print(prev_steps)
        # Consider the values at each candidate step (each is the min no of steps to reach that total).
        candidates = [steps_array[i] for i in prev_steps]
        # Save the minimum candidate + 1 in the current index.
        steps_array[idx] = min(candidates) + 1
        print(steps_array[min(candidates)])

    min_steps = step_array[-1]
    return steps_array


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(sequence(n))
    #sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
