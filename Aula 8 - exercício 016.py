# Desafio 16 - Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira:

"""
#resolução 1:
from math import trunc

n = float(input('digite um número real: '))
nr = trunc(n)
print('o número {} tem a parte inteira {}'.format(n, nr))"""

#resolução 2:
n = float(input('digite um número real: '))
nr = int(n)
print('o número {} tem a parte inteira {}.'.format(n, nr))
