#!/usr/bin/python

# Grab number of lines:
n = int(raw_input())

# Count the words
freq = {}
for x in xrange(0, n):
    s = raw_input()
    if s in freq:
        freq[s] += 1
    else:
        freq.setdefault(s, 1)

# Grab the top how many we are interested in
k = int(raw_input())

# Solve the problem
kTop = [('A', float('-inf'))] * (k+1) # 'A' is the "smallest" letter in the alphabet 
# print kTop

def try_insert(item):
    global kTop, k

    # item[0] = word
    # item[1] = occurences

    kTop[k] = item # Note : This index is not in the "top kTop", it's here because it's handy
    i = k-1
    while (item[1] > kTop[i][1] or (item[1] == kTop[i][1]) and item[0] < kTop[i][0]) and i >= 0:
        # Swap values:
        tmp = kTop[i]
        kTop[i] = kTop[i+1]
        kTop[i+1] = tmp
        # Decrement:
        i -= 1

items = freq.items()
for x in items:
    try_insert(x)

for x in xrange(0, k):
    print kTop[x][0]