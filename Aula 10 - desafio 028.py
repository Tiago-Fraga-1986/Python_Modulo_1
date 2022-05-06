"""Desafio 28 - Escreva um programa que faça o computador "pensar" em um número inteiro entre
0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá revelar na tela se o usuário venceu ou perdeu."""

from random import randint
from time import sleep

a = int(input('O computador escolheu um número de "0" a "5". Tente adivinhar '
              'qual número ele escolheu: '))
e = randint(0, 5)
print('Estou processando a sua resposta...')
sleep(1)  # esse comando adiciona um delay antes da resposta. o número entre () são os segundos de espera.
if e == a:
    print('O número escolhido foi {} e você acertou. Parabéns!'.format(e))
else:
    print('O número escolhido pelo PC foi {} e você escolheu {}. Que pena, você errou...'.format(e, a))
