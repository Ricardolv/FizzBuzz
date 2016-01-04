"""
 Regras do FizzBuzz:

 1_ Se a posição for múltiplo de 3 fizz.
 2_ Se a posição for múltiplo de 5 buzz.
 3_ Se a posição for múltiplo de 3 e 5 fizzbuzz.
 4_ Para qualquer outra pisição vle o proprio número.

"""
from functools import partial
import unittest

multiplo = lambda base, num: num % base == 0
multiplo_3 = partial(multiplo, 3)
multiplo_5 = partial(multiplo, 5)

def robot(pos):
    retorno = str(pos)

    if multiplo_3(pos) and multiplo_5(pos):
        retorno = 'fizzbuzz'
    elif multiplo_3(pos):
        retorno = 'fizz'
    elif multiplo_5(pos):
        retorno = 'buzz'

    return retorno

class fizzbuzzTest(unittest.TestCase):
    def test_say_1_when_1(self):
        self.assertEqual(robot(1), '1')

    def test_say_2_when_2(self):
        self.assertEqual(robot(2), '2')

    def test_say_4_when_4(self):
        self.assertEqual(robot(4), '4')

    def test_say_fizz_when_3(self):
        self.assertEqual(robot(3), 'fizz')

    def test_say_fizz_when_6(self):
        self.assertEqual(robot(6), 'fizz')

    def test_say_fizz_when_9(self):
        self.assertEqual(robot(9), 'fizz')

    def test_say_buzz_when_5(self):
        self.assertEqual(robot(5), 'buzz')

    def test_say_buzz_when_10(self):
        self.assertEqual(robot(10), 'buzz')

    def test_say_buzz_when_20(self):
        self.assertEqual(robot(20), 'buzz')

    def test_say_fizzbuzz_when_15(self):
        self.assertEqual(robot(15), 'fizzbuzz')

    def test_say_fizzbuzz_when_30(self):
        self.assertEqual(robot(30), 'fizzbuzz')

    def test_say_fizzbuzz_when_45(self):
        self.assertEqual(robot(45), 'fizzbuzz')


if __name__ == '__main__':
    unittest.main()
