#!/usr/bin/env python

import sprints
import unittest

class TestSum(unittest.TestCase):

    def test_no_floats_or_ints_in_list(self):
        MeanOfEvenInts, MaxOfFloats = sprints.MyFunc(["sama","sama"])
        self.assertEqual(MeanOfEvenInts, 0, "Should be 0 since no floats or ints in list")
        self.assertEqual(MaxOfFloats, 0, "Should be 0 since no floats or ints in list")

    def test_functionality(self):
        MeanOfEvenInts, MaxOfFloats = sprints.MyFunc([1, 2, 3, 100 ,1.0 ,6.0 , -1.0])
        self.assertEqual(MeanOfEvenInts, 51, "Mean of even int in list: 2, 100 should be 51")
        self.assertEqual(MaxOfFloats, 6.0, "Max of floats in list: 1.0, 6.0, -1.0 should be 6.0")

if __name__ == '__main__':
    unittest.main()