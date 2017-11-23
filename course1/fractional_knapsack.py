# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    """Implement the algorithm straight from the course slides.
    """
    value = 0.
    # Get a sorted list of [value/weight, value, weight]
    values = sorted([[i[0] / i[1]] + list(i) for i in zip(values, weights)], reverse=True)

    for i in values:
        if not capacity:
            return value
        a = min((i[2], capacity))
        value += a * i[0]
        capacity -= a

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
