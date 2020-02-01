# from collections import deque

# def solution(n):
#     """
#     The complexity of dynamic programming solution is too high
#
#     solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
#     6 -> 3 -> 2 -> 1
#     6 -> 5 -> 4
#     6 -> 7 -> 8 -> 4
#     7 -> 6 -> 5 -> 4
#     7 -> 8 -> 4
#     12 -> 6 -> 5 -> 4 -> 2 -> 1
#     12 -> 11 -> 10 -> 9 -> 8 -> 4 -> 2 -> 1
#
#     (1, 0)
#     (2, 1)
#     (3, 2) (4, 2)
#     (4, 3/2) (6, 3) 3 8
#     Each time a x2 occurs,
#
#     :param n: A positive integer as a string.
#     :return: The minimum number of operations needed to transform the number of pellets to 1.
#     """
#     n = int(n)
#     # Solve using a dp solution. Do a depth-first search beginning from 1.
#     # dp[i] is the number of steps to go from 1 to n.
#     # dp[i] = min(dp[i-1], dp[i + 1], dp[i / 2] if i is even) + 1
#     black_nodes = {0: -1}
#     grey_nodes = deque([1])
#     while 1:
#         curr = grey_nodes.popleft()
#         neighbors = [curr + 1, curr - 1]
#         black_nodes[curr] = min(black_nodes.get(nb, float('inf')) for nb in
#                                 (neighbors if curr & 1 else neighbors + [curr / 2])
#                                 if nb in black_nodes) + 1
#         # print 'current', curr, 'neighbors', neighbors, 'dist', dist
#         # print 'current', curr, 'grey_nodes', grey_nodes, 'dist', dist
#         if curr == n:
#             return black_nodes[curr]
#
#         for nb in neighbors:
#             if nb not in black_nodes and nb not in grey_nodes:
#                 grey_nodes.append(nb)
#         grey_nodes.append(curr * 2)

def trailing_zeros(n):
    result = 0
    while n & 1 == 0:
        n, result = n >> 1, result + 1
    return n, result

def solution(n):
    """ Algorithm intuition: The fast descending path for a even number is consecutive division by 2.
    And for even numbers except for 3, addition or subtraction by 1 followed by consecutive division by 2 can result in
        the fastest descent.

    :param n: A positive integer as a string
    :return: The minimum number of operations needed to transform the number of pellets to 1
    """
    n = int(n)
    result = 0
    while n > 1:
        # Special case: can get from 3 to 1 in two subtractions (without division)
        # Thus the algorithm's assumption doesn't hold for 3
        if n == 3:
            return result + 2

        if n & 1 == 0:
            n, num_divs = trailing_zeros(n)
            result += num_divs
        else:
            # Choose between n + 1 and n - 1
            plus, num_divs_plus = trailing_zeros(n - 1)
            minus, num_divs_minus = trailing_zeros(n + 1)
            if num_divs_plus > num_divs_minus:
                n, num_divs = plus, num_divs_plus
            else:
                n, num_divs = minus, num_divs_minus
            result += num_divs + 1
    return result


if __name__ == '__main__':
    print "test_case\t", "solution(test_case)"
    test_cases = [
        '0',  # 0
        '1',  # 0
        '3',  # 2
        '15',  # 5
        '4',  # 2
        '6',  # 4
        '768',  # 10
        '100000'
    ]

    for test_case in test_cases:
        result = solution(test_case)
        print test_case, "\t\t", result
