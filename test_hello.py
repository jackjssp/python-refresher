import unittest
import hello
import numpy as np

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        

    def test_sin(self):
        self.assertAlmostEqual(hello.sin(0), 0, places = 4)
        self.assertAlmostEqual(hello.sin(np.pi), 0, places = 4)
        self.assertAlmostEqual(hello.sin(1), 0.8415, places = 4)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(np.pi), -1)
        self.assertAlmostEqual(hello.cos(1), 0.5403, places = 4)
        
    def test_tan(self):
        self.assertAlmostEqual(hello.tan(0), 0, places = 4)
        self.assertAlmostEqual(hello.tan(np.pi), 0, places = 4)
        hello.tan(np.pi/2).assertRaises(ValueError)
        
    def test_cot(self):
        self.assertAlmostEqual(hello.cot(np.pi/2), 0, places = 4)
        self.assertAlmostEqual(hello.cot(np.pi*3/2), 0, places = 4)
        hello.cot(0).assertRaises(ValueError)

    def test_add(self):
        self.assertEqual(hello.add(1, 1), 2)
        self.assertEqual(hello.add(1, -1), 0)
        self.assertEqual(hello.add(12345, 54321), 66666)

    def test_sub(self):
        self.assertEqual(hello.sub(1, 1), 0)
        self.assertEqual(hello.sub(1, -1), 2)
        self.assertEqual(hello.sub(12345, 54321), -41976)

    def test_mul(self):
        self.assertEqual(hello.mul(1, 1), 1)
        self.assertEqual(hello.mul(3, -2), -6)
        self.assertEqual(hello.mul(-8, -23), 184)

    def test_div(self):
        self.assertEqual(hello.div(1, 1), 1)
        self.assertEqual(hello.div(1, -1), -1)
        self.assertAlmostEqual(hello.div(64, 3), 21.3333, places = 4)

    def test_pow(self):
        self.assertEqual(hello.power(6, 3), 216)
        self.assertAlmostEqual(hello.power(6, -1), 0.1667, places = 4)
        self.assertEqual(hello.power(-2, 5), -32)
    
    def test_root(self):
        self.assertEqual(hello.sqrt(9), 3)
        self.assertAlmostEqual(hello.sqrt(2), 1.414, places = 3)
        self.assertEqual(hello.sqrt(1522756), 1234)

    def test_exp(self):
        self.assertEqual(hello.exp(0), 1)
        self.assertAlmostEqual(hello.exp(2), 7.389, places = 3)
        self.assertAlmostEqual(hello.exp(-3), 0.0498, places = 3)

    def test_log(self):
        self.assertEqual(hello.log(1), 0)
        self.assertAlmostEqual(hello.log(123), 2.0899, places = 4)
        hello.log(0).assertRaises(ValueError)


if __name__ == "__main__":
    unittest.main()
