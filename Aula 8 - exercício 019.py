# Desafio 19: Um professor quer sortear quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
n1 = input('informe o primeiro nome: ')
n2 = input('informe o segundo nome: ')
n3 = input('informe o terceiro nome: ')
n4 = input('informe o quarto nome: ')
print('o nome aluno escolhido foi {}.'.format(choice([n1, n2, n3, n4])))
