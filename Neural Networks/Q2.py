import sys
import numpy as np
import copy

# To justify the correctness of problem 2 from part 1

#  Q2
def linear(width, weights, prev_results):
    curr_results = np.zeros(width)
    for j in range(len(curr_results)):
        for i in range(len(prev_results)):
            curr_results[j] += prev_results[i] * weights[i][j]

    return curr_results


def sigmoid(width, weights, prev_results):
    prev_results = copy.deepcopy(prev_results)
    if prev_results.ndim > 1:
        prev_results = np.asarray(prev_results.T)
        prev_results = prev_results[:, 0]

    curr_results = np.zeros(width)
    curr_results[0] = 1

    for j in range(len(curr_results) - 1):
        y = 0
        for i in range(len(prev_results)):
            y += prev_results[i] * weights[i][j]

        curr_results[j + 1] = 1/(1+np.exp(-y))

    return curr_results


def forward_pass(weights, x, widths, activations):
    shape = []
    for i in range(len(widths)):
        shape.append(np.zeros(widths[i]))

    results = np.array(shape, dtype=object)
    results[0] = x

    for i in range(1, len(results)):
        results[i] = activations[i-1](widths[i], weights[i-1], results[i-1])

    return results


def run_QTwo():
    widths = np.array([3, 3, 3, 1])
    x = np.array([1, 1, 1])
    weights = np.array([
        [[-1, 1], [-2, 2], [-3, 3]],
        [[-1, 1], [-2, 2], [-3, 3]],
        [[-1], [2], [-1.5]]
    ], dtype=object)

    activations = [sigmoid, sigmoid, linear]
    results = forward_pass(weights, x, widths, activations)

    print("Q2 answer:")
    for i in range(1, len(results)-1):
        print(results[i][1])
        print(results[i][2])
    print(results[len(results)-1][0])


if __name__ == '__main__':
    if sys.argv[1] == "Q2":
        run_QTwo()
