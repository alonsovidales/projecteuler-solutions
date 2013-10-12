#!/usr/bin/env python

import fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-10-12"

class Problem:
    __debug = True

    def resolve(self):
        total = 0
        prev = 1
        value = 1
        for pos in range(2, self.__to):
            prev_value = prev
            prev = value
            value += prev_value
            if value % 2 == 0:
                total += value
            if value > self.__to:
                break

        return total

    def __init__(self, to):
        self.__to = int(to)

if __name__ == "__main__":
    print "Up to: "
    print Problem(raw_input()).resolve()
