def solution(s):
    """

    :param s: A string representing employees walking along a hallway.
    :return: The number of times the employees will salute.
    """
    # For each '>', count the number of '<' appears in the right. Sum up the numbers and x2 to get the result.
    # Walk through the string, track how many '>' are encountered. Each time encounter a '<', add the counter to result.
    result, num_right = 0, 0
    for c in s:
        if c == '>':
            num_right += 1
        elif c == '<':
            result += num_right
    return 2 * result


if __name__ == '__main__':
    print "test_case\t", "solution(test_case)"
    test_cases = [">----<", "<<>><", "--->-><-><-->-"]
    for test_case in test_cases:
        print test_case, "\t\t", solution(test_case)
