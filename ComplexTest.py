import ComplexLibrary as cpx
import unittest
import math

class TestLibrary(unittest.TestCase):

    def test_sum(self):
        suma1 = cpx.sumarc((2.3,4.6),(1.4,5.3))
        self.assertAlmostEqual(suma1[0], 3.7)
        self.assertAlmostEqual(suma1[1], 9.9)

        suma2 = cpx.sumarc((3, 5.4), (5.6, 4))
        self.assertAlmostEqual(suma2[0], 8.6)
        self.assertAlmostEqual(suma2[1], 9.4)

    def test_res(self):
        resta1 = cpx.restarc((5.5,2.4),(1.5,3.3))
        self.assertAlmostEqual(resta1[0], 4)
        self.assertAlmostEqual(resta1[1], -0.9)

        resta2 = cpx.restarc((0.7, 2.7), (0.7, 2.7))
        self.assertAlmostEqual(resta2[0], 0)
        self.assertAlmostEqual(resta2[1], 0)

    def test_mult(self):
        mult1 = cpx.multiplicarc((0,1),(0,1))
        self.assertAlmostEqual(mult1[0], -1)
        self.assertAlmostEqual(mult1[1], 0)

        mult2 = cpx.multiplicarc((4, -2.3), (1.6, 3))
        self.assertAlmostEqual(mult2[0], 13.3)
        self.assertAlmostEqual(mult2[1], 8.32)

    def test_div(self):
        div1 = cpx.dividirc((5,-2),(3,1))
        self.assertAlmostEqual(div1[0], 1.3)
        self.assertAlmostEqual(div1[1], -1.1)

        div2 = cpx.dividirc((0, 1), (0, 1))
        self.assertAlmostEqual(div2[0], 1)
        self.assertAlmostEqual(div2[1], 0)

    def test_mod(self):
        self.assertAlmostEqual(cpx.modulo((3,4)), 5)
        self.assertAlmostEqual(cpx.modulo((6,2)), 2*(10**(1/2)))

    def test_fase(self):
        self.assertAlmostEqual(cpx.fase((4,4)),math.pi/4)
        self.assertAlmostEqual(cpx.fase((-4,4)), -math.pi/4)

    def test_conj(self):
        conj1 = cpx.conjugado((5,-2))
        self.assertAlmostEqual(conj1[0], 5)
        self.assertAlmostEqual(conj1[1], 2)

        conj2 = cpx.conjugado((6,7))
        self.assertAlmostEqual(conj2[0], 6)
        self.assertAlmostEqual(conj2[1], -7)

    def test_polar(self):
        polar1 = cpx.polar((3,3))
        self.assertAlmostEqual(polar1[0], 3*(2**(1/2)))
        self.assertAlmostEqual(polar1[1], math.pi/4)

        polar2 = cpx.polar((0, 1))
        self.assertAlmostEqual(polar2[0], 1)
        self.assertAlmostEqual(polar2[1], math.pi/2)

    def test_cartesian(self):
        cart1 = cpx.cartesiano((5,math.pi/2))
        self.assertAlmostEqual(cart1[0], 0)
        self.assertAlmostEqual(cart1[1], 5)

        cart2 = cpx.cartesiano((4, math.pi/6))
        self.assertAlmostEqual(cart2[0], 2*(3**(1/2)))
        self.assertAlmostEqual(cart2[1], 2)

if __name__ == '__main__':
    unittest.main()
