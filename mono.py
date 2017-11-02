#!/usr/bin/env python3

from sys import argv

from globals import *

with open(WFILE, "r") as w:
    weights = [float(line) for line in w]

for name in argv[1:]:
    hd = 0.0
    hn = 0.0
    hi = 0.0
    with open(name, "r") as f:
        values = [float(line) for line in f]
    for i, val in enumerate(values):
        hd = hd + val * weights[i]
        hn = hn + val * weights[N + i]
        hi = hi + val * weights[2 * N + i]

    with open(name.split(".")[0] + ".out", "w") as v:
        v.write("{:f} {:f} {:f}".format(sig(hd), sig(hn), sig(hi))
