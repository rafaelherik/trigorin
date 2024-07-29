from __future__ import annotations
from pathlib import Path

import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    basePath = Path(__file__).parent
    suite = loader.discover(f"{basePath}")
    runner = unittest.TextTestRunner()
    runner.run(suite)
