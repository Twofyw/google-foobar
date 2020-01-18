from random import randint
import time


def solution(xs):
    """
    Iterate over the array and find:
        1. The number of negative numbers.
        2. The number of zeros
        3. The largest negative number.
    If there is an even number of negative numbers, the result is the product of all numbers except for zeros.
    Otherwise, the result is the product of all elements except for the largest negative number.

    :param xs: A list of integers representing the power output levels of each panel in an array.
    :return: The maximum product of some non-empty subset of those numbers.
    """
    if len(xs) == 1:
        return str(xs[0])

    result = 1
    num_zeros, num_neg = 0, 0
    max_neg = -float('inf')
    for x in xs:
        if x == 0:
            num_zeros += 1
        else:
            if x < 0:
                num_neg += 1
                max_neg = max(max_neg, x)
            result *= x

    # Return zero if:
    # 1. If all elements are zero
    # 2. If there is only one elements other than zero and such element is negative
    if num_zeros == len(xs) or (num_neg == 1 and num_zeros == len(xs) - 1):
        return str(0)

    if num_neg & 1:
        result = int(result / max_neg)
    return str(result)

# def solution(xs):
#     """ Solution that handles sparse xs (mostly zeros). Too slow.
#     """
#     xs_nonzero = [x for x in xs if x != 0]
#     if len(xs_nonzero) == 0:
#         return str(0)
#
#     if len(xs_nonzero) == 1:
#         return str(max(xs))
#
#     result = 1
#     num_neg = 0
#     largest_neg = -float('inf')
#     for x in xs_nonzero:
#         result *= x
#         if x < 0:
#             largest_neg = max(largest_neg, x)
#             num_neg += 1
#
#     if num_neg & 1:
#         result = int(result / largest_neg)
#
#     return str(result)


BENCHMARK = False

if __name__ == '__main__':
    print "test_case\t", "solution(test_case)"
    big_array = [randint(-1000, 1000) for _ in range(50)]
    test_cases = [
        [],
        [0],
        [-2],
        [2],
        [0, 0],
        [0, 2],
        [2, 0],
        [-2, 0],
        [-2, 0, 1],
        [-1, 0, 1],
        [0, 0, -8],
        [0, 0, 0],
        [-2, -2, -2, 0],
        [2, 0, 2, 2],
        [-2, -3, 4, -5],
        [-2, -3, -4, -5],
        big_array
    ]

    begin = time.time()
    for o in range(10000):
        for test_case in test_cases:
            result = solution(test_case)
            if not BENCHMARK:
                print test_case, "\t\t", result
    print(time.time() - begin)
