from math import log, ceil

cases = int(raw_input())

for x in xrange(cases):
    coins = int(raw_input())
    weigh_ins = ceil(log(coins, 3))
    print int(weigh_ins)