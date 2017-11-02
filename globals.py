#!/usr/bin/env python3

from math import tanh

sig = tanh
def dsig(x):
    return 1 / (1 + x * x)

WFILE = "weights.dat"
NFILES = 50
N = 100

DECREASE = "1.0 0.0 0.0\n"
NONE = "0.0 1.0 0.0\n"
INCREASE = "0.0 0.0 1.0\n"

LRATE = 0.1
