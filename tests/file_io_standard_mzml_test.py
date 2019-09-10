#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part of pymzml test cases
"""
import os
from pymzml.file_classes.standardMzml import StandardMzml
import unittest
from pymzml.spec import Spectrum, Chromatogram
import test_file_paths
from hypothesis import given
from hypothesis.strategies import integers


class StandardMzmlTest(unittest.TestCase):
    """
    """

    def setUp(self):
        """
        """
        paths = test_file_paths.paths
        self.standard_mzml = StandardMzml(paths[0], "latin-1")

    def tearDown(self):
        """
        """
        self.standard_mzml.close()

    def test_getitem(self):
        """
        """
        ID = 8
        spec = self.standard_mzml[ID]
        self.assertIsInstance(spec, Spectrum)
        target_ID = spec.ID
        self.assertEqual(ID, target_ID)

        ID = "TIC"
        chrom = self.standard_mzml[ID]
        self.assertIsInstance(chrom, Chromatogram)
        self.assertEqual(ID, chrom.ID)

    # @given(integers(min_value=1, max_value=10))
    # def test_interpol_search(self, choice):
    #     """
    #     """
    #     spec = self.standard_mzml._interpol_search(choice)
    #     self.assertIsInstance(spec, Spectrum)
    #     self.assertEqual(spec.ID, choice)

    @given(integers(min_value=1, max_value=10))
    def test_binary_search(self, choice):
        """
        """
        spec = self.standard_mzml._binary_search(choice)
        self.assertIsInstance(spec, Spectrum)
        self.assertEqual(spec.ID, choice)

if __name__ == '__main__':
    unittest.main(verbosity=3)
