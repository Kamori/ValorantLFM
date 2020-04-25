# -*- coding: utf-8 -*-

import unittest

from .context import sample


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def testadd(self):
        self.assertEqual(sample.add(1, 2), 3)
        self.assertNotEqual(sample.add(0, 2), 1)


if __name__ == "__main__":
    unittest.main()
