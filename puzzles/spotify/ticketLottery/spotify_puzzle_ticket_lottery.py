#!/usr/bin/python

"""
Author: TD
License: GPLv3
"""

from math import ceil

# Too slow or overflows with huge values (factorial is factorial!)
# def binomial(m, k):
#     return (float(factorial(m))) / (float(factorial(k) * factorial(m-k)))
def binomial(m, k):
        if 0 <= k and k <= m:
            res = 1
            for x in xrange(min(k, m - k)):
                res = res * (m-x) // (x+1)
            return res
        else:
            return 0

def hypergeo(n, d, m, k):
    return binomial(m, k) * binomial(n-m, d-k) / float(binomial(n, d))


if __name__ == '__main__':
    population, draws, t, group_population = [int(_) for _ in raw_input().strip().split(" ")]

    p = 0.0
    # proba = proba of having the exact number of successes + proba of having more than necessary successes
    for k in xrange(int(ceil(group_population/float(t))), group_population+1):
        p += hypergeo(population, group_population, draws, k)
    print '%0.10f' % p