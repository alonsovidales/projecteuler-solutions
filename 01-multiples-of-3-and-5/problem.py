#!/usr/bin/env python

import fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-10-12"

class Problem:
    __debug = True

    def resolve(self):
        total = 0
        for number in range(self.__number):
            if number % 3 == 0 or number % 5 == 0:
                total += number

        return total

    def __init__(self, number):
        self.__number = int(number)

if __name__ == "__main__":
    print "Up to: "
    print Problem(raw_input()).resolve()
