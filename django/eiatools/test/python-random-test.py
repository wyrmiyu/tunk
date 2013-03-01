#!/usr/bin/env python

from random import randint
from decimal import Decimal

res = {}
turn = 0
precision = 1000000000

total_zero = 180
win_zero = 74

total = Decimal(total_zero)
win = Decimal(win_zero)


while win > 0:
    turn = turn + 1
    target = int( win / total * precision )
    d = randint(1,precision)
    if d in res:
        res[d] = res[d] + 1
    else:
        res[d] = 1
    if d <= target:
        win = win - 1
        step = win_zero - win
        print "Turn %s: Viva la Revolution! Step %s" % (turn, step)
    else:
        print "Turn %s: No event." % turn
    total = total - 1

print "Turns: %s" % turn

for k, v in res.items():
    print "Rolled %ss %s times" % (k, v)

print "Min: %s (%s times)" % (min(res.keys()), min(res.values()))
print "Max: %s (%s times)" % (max(res.keys()), max(res.values()))
