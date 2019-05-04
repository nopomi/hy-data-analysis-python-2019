#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_out

module_name="src.reverse_dictionary"
reverse_dictionary = load(module_name, "reverse_dictionary")

@points('p01-13.1')
class ReverseDictionary(unittest.TestCase):

    
    def test_first(self):
        d={"move":["liikuttaa"], "hide":["piilottaa", "salata"]}
        r=reverse_dictionary(d)
        self.assertEqual(r["liikuttaa"], ["move"])
        self.assertEqual(r["piilottaa"], ["hide"])
        self.assertEqual(r["salata"], ["hide"])
        self.assertEqual(len(r), 3)

    def test_second(self):
        d={"move":["liikuttaa"], "hide":["piilottaa", "salata"], "six":["kuusi"], "fir":["kuusi"]}
        r=reverse_dictionary(d)
        self.assertEqual(r["liikuttaa"], ["move"])
        self.assertEqual(r["piilottaa"], ["hide"])
        self.assertEqual(r["salata"], ["hide"])
        self.assertEqual(set(r["kuusi"]), set(["fir", "six"]))
        self.assertEqual(len(r), 4)




if __name__ == '__main__':
    unittest.main()
    
