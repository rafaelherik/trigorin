from __future__ import annotations
from terraform import *
import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('.')
    print("Running the test cases.")
    print(suite)
    runner = unittest.TextTestRunner()
    runner.run(suite)


