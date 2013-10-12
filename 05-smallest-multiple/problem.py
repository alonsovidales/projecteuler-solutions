#!/usr/bin/env python

import random
import math

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-10-12"

class Problem:
    __debug = True

    def resolve(self):
        num = 2520
        while True:
            num += 1
            possible = True
            for check in range(1, 21):
                if num % check != 0:
                    possible = False
                    break

            if possible:
                return num

if __name__ == "__main__":
    print "Calculating..."
    print Problem().resolve()
