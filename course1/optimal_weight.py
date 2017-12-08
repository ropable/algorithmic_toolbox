# Uses python3
import sys


def optimal_weight(W, w):
    '''Implement the algorithm from the course slides (Knapsack w/o repetitions).
    W: capacity of knapsack
    w: list of weights.
    Value is assumed as 1:1 with weight.
    '''
    w = [0] + w  # Extend w with a zero-weight element (first row & column).
    # Create an array to contain the knapsack weights.
    weight = [[0 for j in range(1, W+2)] for i in range(1, len(w)+1)]
    # Iterate through each of the weights.
    for i in range(1, len(w)):
        # Iterate through each capacity from 1 to W.
        for j in range(1, W+1):  # Note: range() is exclusive (hence W+1).
            weight[i][j] = weight[i-1][j]  # Set the cell weight equal to the row above, same column.
            if w[i] <= j:  # If the current weight is less than or equal to the current capacity...
                val = weight[i-1][j-w[i]] + w[i]  # Set a value: weight of the row above, column (capacity-current capacity) plus current capacity.
                if weight[i][j] < val:  # If the current array value is less than calculated value, replace it.
                    weight[i][j] = val

    # Return the final row, column weight.
    return weight[len(w)-1][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
