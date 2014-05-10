#!/usr/bin/python

"""
This is an algorithm to solve the problem of the http://en.wikipedia.org/wiki/Change-making_problem
This algorithm was made completely without looking at the literature and might or might not resemble
or even be completely the same as some previously described algorithm!

It is a greedy bactracking algorithm and might or might not be exact. But it should be.

Its complexity is pseudo-polynomial as follows:

A = total amount of change to give back to customer
number of different sorts of coins = len(Wallet) if defined as below
min(wallet coins values) = min(Wallet) if defined as below
worst case number of function calls = A / min(wallet coins values) * number of different sorts of coins 

In other words, it grows linearly with the amout of change. The bigger the coins values and the less
number of calls will be needed, and the higher the number of sorts of coins and the higher
the number of calls.

THAT IN THE WORST CASE. In practice, I am not (yet) able to analyze its average complexity.
"""

# Note: Everything has to be integers so that we do not have floating point representation
# errors
# Here for instance everything is multiplied by 10
# Note that we use the dictionary syntax for human input
# but a list of lists is much easier to manipulate later in the problem
# so we just convert it once at the beginning :) 
# /!\ THE RESULTING LIST HAS TO BE SORTED BY DESCENDING ORDER OF THE
# COIN VALUES OR THE ALGORITHM WILL _NOT_ WORK /!\
Wallet = sorted([[_[0], _[1]] for _ in {
    1000: 10,
    500: 2,
    20: 20,
    10: 8,
    2: 10,
    5: 10
}.items()], reverse=True)

DBG = False

def d(*args):
    if not DBG:
        return
    print args

EMPTY = -42
def solve_greedy_backtrack(wallet, series, cursor, remainder):
    d("sgb")
    if remainder is 0:
        return None
    elif not wallet:
        d("The wallet is empty and there is a remainder, this is not doable...")
        return EMPTY
    elif remainder < wallet[-1][0]:
        # There is nothing inside our wallet that could fit in this remainder
        d("The smallest value we have is", wallet[-1][0], "and we have a remainder of", remainder)
        return False
    else:
        # As long as the top value of the wallet does not fit in the remainder
        # Important note: We do not need to check for new_cursor going over len(wallet)
        # because we checked that the smallest value (wallet is sorted) would indeed fit
        # so this loop WILL stop before passing the end of the list
        new_cursor = cursor
        while remainder < wallet[new_cursor][0]:
            # skip it
            new_cursor += 1

        # Now, we have popped everything that does not fit in the remainder, we have found the 
        # value that fits inside
        wallet[new_cursor][1] -= 1
        remainder -= wallet[new_cursor][0]
        series.append(wallet[new_cursor][0])
        if wallet[new_cursor][1] is 0:
            # We finished all our coins of this value
            wallet.pop(new_cursor)
        if remainder > 0:
            d("Remainder:", remainder)
            while True:
                d("series", series)
                res = solve_greedy_backtrack(wallet, series, new_cursor, remainder)
                if res is EMPTY:
                    return EMPTY
                elif res is not None:
                    d("Backtracking")
                    # We did not find a path to the solution, we have to backtrack
                    # We remove the last added coin
                    # and put the remainder value back to before this coin was added
                    remainder += series.pop(-1)
                    # And we remove the biggest coins of this value, as this branch of the 
                    # tree will go nowhere
                    wallet.pop(new_cursor)
                else:
                    return None

def solve(wallet, sum_to_reach):
    w = wallet[:]
    series = []
    res = solve_greedy_backtrack(w, series, 0, sum_to_reach)
    if res is None:
        return series
    return None

if __name__ == '__main__':
    import sys
    if len(sys.argv) is not 2:
        print "Usage: ./change_making.py sum_to_reach"
        sys.exit()
    print "Solving..."
    print "Using wallet:", Wallet
    print "Solved:", solve(Wallet, int(sys.argv[1]))
