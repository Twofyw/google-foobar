""" Solution for Google Foobar problem 1"""

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    Maps composites to primes witnessing their compositeness.
    This is memory efficient, as the sieve is not "run forward"
    indefinitely, but only as long as required by the current
    number being tested.
    """
    # Sieve of Eratosthenes
    # Code by David Eppstein, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations

            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers

            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def solution(i):
    """

    :param i: The starting index n of Lambda's string of all primes
    :return: The next five digits in the string from position i
    """
    prime_string = ''
    for q in gen_primes():
        if len(prime_string) - 1 > i + 5:
            break
        prime_string += str(q)
    return prime_string[i:i+5]


if __name__ == '__main__':
    print "test_case\t", "solution(test_case)"
    for test_case in [-1, 0, 3, 5, 100, 10000, 100000]:
        print test_case, '\t\t', solution(test_case)
