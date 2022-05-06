""" Desafio 30 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR
 ou IMPAR. """
n = int(input('digite um número inteiro: ')) % 2
#pi = n % 2
#if pi > 0:
if n > 0:
    print('O número {} é impar'. format(n))
else:
    print('O número {} é par.'. format(n))
