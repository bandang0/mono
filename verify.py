#!/usr/bin/env python3

from sys import argv

from globals import *

for name in argv[1:]:
    with open(name, "r") as f:
        values = []
        for line in f:
            values.append(float(line))
        if sorted(values) == values:
            toWrite = INCREASE
        elif sorted([-x for x in values]) == [-x for x in values]:
            toWrite = DECREASE
        else:
            toWrite = NONE

    with open(name.split(".")[0] + ".ver", "w") as v:
        v.write(toWrite)
