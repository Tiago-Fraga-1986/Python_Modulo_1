# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.
#resolução com shuffle
from random import shuffle
a1 = input('informe o nome do aluno 1: ')
a2 = input('informe o nome do aluno 2: ')
a3 = input('informe o nome do aluno 3: ')
a4 = input('informe o nome do aluno 4: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A sequência de apresentação será: {}'.format(lista))

''' #resolução com sample
from random import sample
a1 = input('informe o nome do aluno 1: ')
a2 = input('informe o nome do aluno 2: ')
a3 = input('informe o nome do aluno 3: ')
a4 = input('informe o nome do aluno 4: ')
ordem = sample([a1, a2, a3, a4,], 4)
print('a ordem escolhida foi {}.'.format(ordem)) '''
