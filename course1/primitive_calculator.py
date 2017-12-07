# Uses python3
import sys


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
    print(steps_array)
    for idx in range(2, len(steps_array)):
        # idx is the value that we need to calculate the optimal no of steps to reach.
        # Find all the candidate previous paths ().
        prev_steps = [idx - 1]  # idx - 1 is always a path option.
        # If idx is divisible by 2 or 3, consider those as paths.
        if idx % 2 == 0:
            prev_steps.append(idx // 2)
        if idx % 3 == 0:
            prev_steps.append(idx // 3)
        print(prev_steps)
        # Consider the values at each candidate step (each is the min no of steps to reach that total).
        candidates = [steps_array[i] for i in prev_steps]
        print(candidates)
        # Save the minimum candidate + 1 in the current index.
        steps_array[idx] = min(candidates) + 1
        print(steps_array)

    return steps_array

    return sequence


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
