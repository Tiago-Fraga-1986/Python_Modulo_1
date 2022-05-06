# Desafio 17 - Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triangulo retângulo. Calcule e mostre o comprimento da hipotenusa.

"""#Resolução manual:
co = float(input('informe o comprimento do Cateto Oposto: '))
ca = float(input('informe o comprimento do Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A Hipotenusa dos Catetos {} e {} é de {:.2f}.'.format(co, ca, hi))"""

# Resolução com importação de Biblioteca:
from math import hypot

co = float(input('Informe o comprimento do Cateto Oposto: '))
ca = float(input('Informe o comprimento do Cateto Adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa dos Catetos {} e {} é de {:.2f}.'.format(co, ca, hip))
