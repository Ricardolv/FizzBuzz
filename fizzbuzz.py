"""
 Regras do FizzBuzz:

 1_ Se a posição for múltiplo de 3 fizz.
 2_ Se a posição for múltiplo de 5 buzz.
 3_ Se a posição for múltiplo de 3 e 5 fizzbuzz.
 4_ Para qualquer outra pisição vle o proprio número.

"""
from functools import partial

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


