#!/usr/bin/env python3

import numpy as np
import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_out

module_name="src.interleave"
interleave = load(module_name, "interleave")

@points('p01-11.1')
class Interleave(unittest.TestCase):

    
    def test_first(self):
        L1=[1,2,3]
        L2=[20,30,40]
        L3=['a', 'b', 'c']
        result = interleave(L1, L2, L3)
        self.assertEqual(result, [1, 20, 'a', 2, 30, 'b', 3, 40, 'c'], msg="Incorrect result for input lists %s, %s, %s!" % (L1, L2, L3))

    def test_random(self):
        n = 4
        size=50
        LL = []
        for i in range(n):
            L=list(np.random.randint(-100, 100, size))
            LL.append(L)
        result = interleave(*LL)
        self.assertEqual(len(result), n * size, msg="Incorrect result list length!")
        for i in range(n):
            self.assertEqual(LL[i], result[i::n], msg="Input lists are not correctly interleaved!")

if __name__ == '__main__':
    unittest.main()
    
