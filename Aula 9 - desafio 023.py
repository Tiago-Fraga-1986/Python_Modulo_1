# Desafio 23 - Faça um programa que leia um número de "0" a "9999"
# e mostre na tela cada um dos dígitos separados:
"""Solução String"""
n = (input('Informe um número de "0" a "9999": '))
nc = '0000' + n
print('o número {} possui os seguintes dados: \nunidade {}\ndezena {}\ncentena {}\nmilhar {}'
      .format(n, nc[-1], nc[-2], nc[-3], nc[-4]))

"""Solução matemática:
n = input('Informe um número de "0" a "9999": '
un = n // 1 % 10
dz = n // 10 % 10
cn = n // 10 % 10
ml = n // 10 % 10
no print é a mesma coisa, somente colocando os objetos correspondentes."""
