"""Desafio 014 - Desenvolva um código que receba uma temperatura em ºC e converta esta em ºF"""
c = float(input('Informe a temperatura em ºC: '))
f = ((c * 9) / 5) + 32
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF.'.format(c, f))
