import time


def solution(l):
    """
    Is l sorted?

    :param l:
    :return:
    """
    lucky_tuples = {}
    for i, o in enumerate(l):
        seconds = []
        for j, p in enumerate(l[i+1:]):  # Can be optimized to reuse it's factors
            if p % o == 0:
                seconds.append(((i + 1) + j, p))
        # print('seconds', seconds)
        lucky_tuples[(i, o)] = seconds
    # print('lucky_tuples', lucky_tuples)

    # build triplets
    time.sleep(1)
    lucky_triplets = []
    for i, first in enumerate(l):
        # print('first', first, lucky_tuples[first])
        for j, second in lucky_tuples[(i, first)]:
            # print('second', second)
            for k, third in lucky_tuples[(j, second)]:
                lucky_triplets.append((first, second, third))
    return len(lucky_triplets)


if __name__ == '__main__':
    print "test_case\t", "solution(test_case)"
    test_cases = [
        [1, 1, 1],  # 1
        [1, 1, 1],  # 1
        [1, 2, 3, 4, 5, 6],  # 3
    ]

    for test_case in test_cases:
        result = solution(test_case)
        print test_case, "\t\t", result
