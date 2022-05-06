"""Desafio 006 - Crie um programa que leia um número real e informe:
# Seu dobro
# seu triplo
# a raiz quadrada"""
n = int(input('Informe um número real: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('Você escolheu o número {}. \n'
      'O dobro de {} é {}; \n'
      'O triplo é {}; \n '
      'A raiz quadrada é {:.2f}.'.format(n, n, d, t, r))
#Do mesmo modo que no desafio 5, as operações podem ser feitas dentro do ".format", porém isso não é
#recomendado caso vá usar essas mesmas variáveis durante o script. podemos usar também, para a
#raiz, o comando ".pow", da seguinte forma:
#r = pow(n, (1/2))