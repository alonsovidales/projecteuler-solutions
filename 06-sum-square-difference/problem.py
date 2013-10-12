#!/usr/bin/env python

import random
import math

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-10-12"

class Problem:
    __debug = True

    def resolve(self):
        num_sqr = 0
        num_sum = 0
        for count in range(1, 101):
            num_sum += count
            num_sqr += count ** 2

        return num_sum ** 2 - num_sqr

if __name__ == "__main__":
    print "Calculating..."
    print Problem().resolve()
