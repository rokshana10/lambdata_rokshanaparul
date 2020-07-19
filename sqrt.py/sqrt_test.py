import unittest
from sqrt import newton_sqrt1, lazy_sqrt, bulitin_sqrt

class sqrttest(unittest, TestCase):
    '''Class to test square root functions'''

    def test_lazy_sqrt(self):
        self.assertEqual(lazy_sqrt(9), 3)

    def test_newton_sqrt1(self):
        self.assertAlmostEqual(newton_sqrt1(2), 1.4142135)

 if __name__ == "__main__":
    unittest.main() 
      pip install -i https://test.pypi.org/simple/ lambdata-rokshanaparul    