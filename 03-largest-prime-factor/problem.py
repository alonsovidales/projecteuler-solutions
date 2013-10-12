#!/usr/bin/env python

import random
import math

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-10-12"

class Problem:
    __debug = True

    def get_possible(self, to):
        for num in range(int(math.sqrt(to)), 1, -1):
            if self.__to % num == 0:
                yield num

    def resolve(self):
        for max_num in self.get_possible(self.__to):
            # use the Fermat's Little Theorem to know if is a possible prime num
            if (3 ** (max_num - 1)) % max_num == 1:
                prime = True
                for div in xrange(2, max_num):
                    if max_num % div == 0 and max_num != div:
                        prime = False
                        break

                if prime:
                    return max_num

        return -1

    def __init__(self, to):
        self.__to = int(to)

if __name__ == "__main__":
    print "Up to: "
    print Problem(raw_input()).resolve()
