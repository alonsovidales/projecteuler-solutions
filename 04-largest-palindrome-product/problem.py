#!/usr/bin/env python

import random
import math

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-10-12"

class Problem:
    __debug = True

    def resolve(self):
        max_pal = 0
        for left in xrange(999, 0, -1):
            for right in range(999, 0, -1):
                aux = str(left * right)

                if aux == aux[::-1] and int(aux) > max_pal:
                    max_pal = int(aux)

        return max_pal

if __name__ == "__main__":
    print "Calculating..."
    print Problem().resolve()
