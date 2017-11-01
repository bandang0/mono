#!/usr/bin/env python3

import random

from globals import *

for i in range(NFILES):
    random.seed()
    with open("data/f" + str(i) + ".dat", "w") as f:
        for j in range(N):
            f.write(str(random.random()) + "\n")
