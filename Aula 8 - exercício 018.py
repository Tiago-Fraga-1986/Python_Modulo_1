# Desafio 18 - Faça um programa que leia um angulo qualquer e mostre na tela o valor de
# Seno, Cosseno e Tangente desse angulo:
from math import radians, sin, cos, tan
a = float(input('digite um angulo qualquer: '))
an = radians(a)
print('seguem os valores relativos ao angulo {}:\n'
      'Seno: {:.2f}\n'
      'Cosseno: {:.2f}\n'
      'Tangente: {:.2f}\n'.format(a, sin(an), cos(an), tan(an)))
