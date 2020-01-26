import time

def solution(l):
    result = 0
    dp = [0] * len(l)
    for i in xrange(len(l) - 1):
        for j in xrange(i + 1, len(l)):
            if l[j] % l[i] == 0:
                dp[j] += 1
                result += dp[i]
    return result

# def solution(l):
#     """
#     Is l sorted?
#
#     :param l:
#     :return:
#     """
#     lucky_tuples = {}
#     lucky_tuples_inv = {}
#     for i, o in enumerate(l):
#         seconds = []
#         if o in lucky_tuples_inv:
#             for j, p in lucky_tuples[lucky_tuples_inv[o]]:
#                 if p % o == 0:
#                     seconds.append((j, p))
#         else:
#             firsts = []
#             for j, p in enumerate(l[i+1:]):  # Can be optimized to reuse it's factors
#                 if p % o == 0:
#                     seconds.append(((i + 1) + j, p))
#         # print('seconds', seconds)
#         lucky_tuples[(i, o)] = seconds
#     # print('lucky_tuples', lucky_tuples)
#
#     # build triplets
#     time.sleep(1)
#     lucky_triplets = []
#     for i, first in enumerate(l):
#         # print('first', first, lucky_tuples[first])
#         for j, second in lucky_tuples[(i, first)]:
#             # print('second', second)
#             for k, third in lucky_tuples[(j, second)]:
#                 lucky_triplets.append((first, second, third))
#     return len(lucky_triplets)


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
