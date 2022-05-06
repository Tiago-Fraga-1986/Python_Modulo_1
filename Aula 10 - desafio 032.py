""" Desafio 32 - Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO."""
from calendar import isleap

a = int(input('informe o ano: '))
b = isleap(a)
if b:
    print('o ano {} é Bissexto.'.format(a))
else:
    print('o ano {} não é Bissexto.'.format(a))
