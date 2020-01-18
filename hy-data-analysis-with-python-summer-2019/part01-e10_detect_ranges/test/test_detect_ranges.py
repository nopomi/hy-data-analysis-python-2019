#!/usr/bin/env python3

import numpy as np
import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_out

module_name="src.detect_ranges"
detect_ranges = load(module_name, "detect_ranges")

@points('p01-10.1')
class DetectRanges(unittest.TestCase):


    def test_first(self):
        L = [2,5,4,8,12,6,7,10,13]
        Lc = L.copy()
        result = detect_ranges(L)
        self.assertEqual(L, Lc, msg="Do not modify the input list %s!" % Lc)
        self.assertEqual(result, [2, (4, 9), 10, (12, 14)], msg="Incorrect result for the input list %s!" % L)

    def test_random(self):
        for i in range(10):
            L = list(set(np.random.randint(-100, 100, 10)))
            mi = min(L)
            ma = max(L)
            complement = list(set(range(mi, ma+1)) - set(L))
            result = detect_ranges(L)
            complement_result = detect_ranges(complement)
            catenation = []   # Expand the ranges into this catenation, contains all the elements in the ranges
            for x in result:
                try:
                    a, b = x
                    catenation.extend(range(a,b))
                except TypeError:
                    catenation.append(x)
            self.assertEqual(sorted(L), catenation, msg="Wrong result for input list %s!" % L)
            self.assertEqual(len(result), len(complement_result)+1, msg="Wrong result for input list %s!" % L)


if __name__ == '__main__':
    unittest.main()

