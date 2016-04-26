#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python_configuration
----------------------------------

Tests for `python_configuration` module.
"""

import unittest
from pyconfiguration import Configuration


class TestPyConfiguration(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_load_json_1(self):
        Configuration.load_config("config1.json")
        self.assertEquals(Configuration.a, 1)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
