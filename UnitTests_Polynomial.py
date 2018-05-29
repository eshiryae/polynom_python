import unittest
from Polynomial import Polynomial

class UnitTests_Polynomial(unittest.TestCase):
    def test_initEmptyList(self):
        p0 = Polynomial([])

        self.assertEqual(p0.coeffs, [0])
        self.assertEqual(p0.degree, 0)

    def test_init(self):
        p0 = Polynomial([5, 4])
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([10, -1, 3, 2])
        p3 = Polynomial(p1)
        p4 = Polynomial(1)
        p5 = Polynomial(1.5)

        self.assertEqual(p0.coeffs, [5, 4])
        self.assertEqual(p0.degree, 1)
        self.assertEqual(p1.coeffs, [1, 2, 3])
        self.assertEqual(p1.degree, 2)
        self.assertEqual(p2.coeffs, [10, -1, 3, 2])
        self.assertEqual(p2.degree, 3)
        self.assertEqual(p3.coeffs, [1, 2, 3])
        self.assertEqual(p3.degree, 2)
        self.assertEqual(p4.coeffs, [1])
        self.assertEqual(p4.degree, 0)
        self.assertEqual(p5.coeffs, [1.5])
        self.assertEqual(p5.degree, 0)

    def test_initWithError(self):
        with self.assertRaises(TypeError) as context:
            p0 = Polynomial('a')
        self.assertEqual(str(context.exception),"('Wrong or unsupported type of argument(must be const(int, float) or Polynomial): ', 'a')")
        with self.assertRaises(TypeError) as context:
            p0 = Polynomial([1, 'a'])
        self.assertEqual(str(context.exception),"('Wrong or unsupported type of argument(must be const(int, float) or Polynomial): ', 'a')")
        with self.assertRaises(TypeError) as context:
            p0 = Polynomial([1, (2, 3)])
        self.assertEqual(str(context.exception),"('Wrong or unsupported type of argument(must be const(int, float) or Polynomial): ', (2, 3))")
        with self.assertRaises(TypeError) as context:
            p0 = Polynomial([1, 2, [3, 4]])
        self.assertEqual(str(context.exception),"('Wrong or unsupported type of argument(must be const(int, float) or Polynomial): ', [3, 4])")
        with self.assertRaises(TypeError) as context:
            p = "2x+1"
            p0 = Polynomial(p)
        self.assertEqual(str(context.exception),"('Wrong or unsupported type of argument(must be const(int, float) or Polynomial): ', '2x+1')")


    def test_deleteZeros(self):
        p0 = Polynomial([0, 1, 0, 3])
        p1 = Polynomial([0, 0.0, 1, 2])
        p2 = Polynomial([0, 0.0, 0, 1])
        p3 = Polynomial([0, 0.0, 0, 0])
        self.assertEqual(p0.coeffs, [1, 0, 3])
        self.assertEqual(p0.degree, 2)
        self.assertEqual(p1.coeffs, [1, 2])
        self.assertEqual(p1.degree, 1)
        self.assertEqual(p2.coeffs, [1])
        self.assertEqual(p2.degree, 0)
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)


    def test_add(self):
        p0 = Polynomial([1, 2.5, -3])
        p1 = 4
        p2 = Polynomial([])
        p3 = Polynomial([-1, -2.5, 3])
        p4 = Polynomial([1, 2, 3, 4])
        p5 = Polynomial([1, 2])

        res = p0 + p1
        self.assertEqual(res.coeffs, [1, 2.5, 1])
        self.assertEqual(res.degree, 2)
        res = p1 + p0
        self.assertEqual(res.coeffs, [1, 2.5, 1])
        self.assertEqual(res.degree, 2)
        res = p0 + p2
        self.assertEqual(res.coeffs, [1, 2.5, -3])
        self.assertEqual(res.degree, 2)
        res = p0 + p3
        self.assertEqual(res.coeffs, [0])
        self.assertEqual(res.degree, 0)
        res = p0 + p4
        self.assertEqual(res.coeffs, [1, 3, 5.5, 1])
        self.assertEqual(res.degree, 3)
        res = p0 + p5
        self.assertEqual(res.coeffs, [1, 3.5, -1])
        self.assertEqual(res.degree, 2)
        p0 += p5
        self.assertEqual(p0.coeffs, [1, 3.5, -1])
        self.assertEqual(p0.degree, 2)

    def test_addWithError(self):
        p0 = Polynomial([1, 2, 3])
        p1 = '2x+1'
        with self.assertRaises(TypeError) as context:
            p0 + p1
        self.assertEqual(str(context.exception),"('Wrong or unsupported type of argument(must be const(int, float) or Polynomial): ', '2x+1')")

    def test_negative(self): # -(Polynomial)
        p0 = Polynomial([1, -2, 3.5, 0, -5.5])
        p1 = -p0
        self.assertEqual(p0.coeffs, [1, -2, 3.5, 0, -5.5])
        self.assertEqual(p0.degree, 4)
        self.assertEqual(p1.coeffs, [-1, 2, -3.5, 0, 5.5])
        self.assertEqual(p1.degree, 4)

    #substraction
    def test_sub(self):
        p0 = Polynomial([1, 2.5, -3])
        p1 = 4
        p2 = Polynomial([])
        p3 = Polynomial([1, 2.5, -3])
        p4 = Polynomial([1, 2, 3, 4])
        p5 = Polynomial([1, 2])

        res = p0 - p1
        self.assertEqual(res.coeffs, [1, 2.5, -7])
        self.assertEqual(res.degree, 2)
        res = p1 - p0
        self.assertEqual(res.coeffs, [-1, -2.5, 7])
        self.assertEqual(res.degree, 2)
        res = p0 - p2
        self.assertEqual(res.coeffs, [1, 2.5, -3])
        self.assertEqual(res.degree, 2)
        res = p0 - p3
        self.assertEqual(res.coeffs, [0])
        self.assertEqual(res.degree, 0)
        res = p0 - p4
        self.assertEqual(res.coeffs, [-1, -1, -0.5, -7])
        self.assertEqual(res.degree, 3)
        res = p0 - p5
        self.assertEqual(res.coeffs, [1, 1.5, -5])
        self.assertEqual(res.degree, 2)
        p0 -= p5
        self.assertEqual(p0.coeffs, [1, 1.5, -5])
        self.assertEqual(p0.degree, 2)

    def test_subWithError(self):
        p0 = Polynomial([1, 2, 3])
        p1 = '2x+1'
        with self.assertRaises(TypeError) as context:
            p0 - p1
        self.assertEqual(str(context.exception),"('Wrong or unsupported type of argument(must be const(int, float) or Polynomial): ', '2x+1')")

    def test_mul(self):
        p0 = Polynomial([1, 2.5, -3])
        p1 = 4
        p2 = Polynomial([])
        p3 = Polynomial([1, 2.5, -3])
        p4 = Polynomial([1, 2])

        res = p0 * p1
        self.assertEqual(res.coeffs, [4, 10, -12])
        self.assertEqual(res.degree, 2)
        res = p1 * p0
        self.assertEqual(res.coeffs, [4, 10, -12])
        self.assertEqual(res.degree, 2)
        res = p0 * p2
        self.assertEqual(res.coeffs, [0])
        self.assertEqual(res.degree, 0)
        res = p0 * p3
        self.assertEqual(res.coeffs, [1, 5, 0.25, -15, 9])
        self.assertEqual(res.degree, 4)
        res = p0 * p4
        self.assertEqual(res.coeffs, [1, 4.5, 2.0, -6])
        self.assertEqual(res.degree, 3)
        p0 *= 2
        self.assertEqual(p0.coeffs, [2, 5, -6])
        self.assertEqual(p0.degree, 2)

    def test_mulWithError(self):
        p0 = Polynomial([1, 2, 3])
        p1 = '2x+1'
        with self.assertRaises(TypeError) as context:
            p0 * p1
        self.assertEqual(str(context.exception),"('Wrong or unsupported type of argument(must be const(int, float) or Polynomial): ', '2x+1')")

    def test_equalPolynomials(self):
        p0 = Polynomial([1, 2, 3])
        p1 = "x^2+2x+3"
        p2 = p0
        p3 = Polynomial([4])
        p4 = 4
        p5 = Polynomial([-4])


        self.assertTrue(p0 == p1)
        self.assertTrue(p0 == p2)
        self.assertFalse(p0 == p3)
        self.assertTrue(p3 == p4)
        self.assertFalse(p3 == p5)


    def test_notEqualPolynomials(self):
        p0 = Polynomial([1, 2, 3])
        p1 = "x^2+2x+3"
        p2 = p0
        p3 = Polynomial([4])
        p4 = 4
        p5 = Polynomial([-4])

        self.assertFalse(p0 != p1)
        self.assertFalse(p0 != p2)
        self.assertTrue(p0 != p3)
        self.assertFalse(p3 != p4)
        self.assertTrue(p3 != p5)

    def test_strPolynomial(self):
        p0 = Polynomial([])
        p1 = Polynomial([0, 0.0, 0])
        p2 = Polynomial([1, -2, 0, 4.5])
        p3 = Polynomial([-1, -2, 3, 0, 1, 1])

        self.assertEqual(str(p0), "0")
        self.assertEqual(str(p1), "0")
        self.assertEqual(str(p2), "x^3-2x^2+4.5")
        self.assertEqual(str(p3), "-x^5-2x^4+3x^3+x+1")





if __name__ == '__main__':
    unittest.main()