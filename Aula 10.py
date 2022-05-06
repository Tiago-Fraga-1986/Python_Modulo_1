"""Aula 10 - Estrutura Condicional

As estruturas condicionais são compostas de blocos, onde, a partir de um comando de entrada,
o programa é condicionado a seguir determinados conjuntos de instruções. Os blocos são colocados
dentro do script um passo mais para a direita dos comandos, usando a tecla Tab.
ex.:

if carro.esquerda():
    bloco True
else:
    bloco False

Exemplo prático: Escreva um programa que pergunte qual a idade do carro do usuário. Caso o carro
tenha 3 anos ou menos, elogie. Se tiver mais de 3 anos, avise que está na hora de trocar de carro:

t = int(input('Qual a idade do seu carro? '))
if t > 3:
    print('Que troço brabo! Tá na hora de vender isso aí, cariado!')
else:
    print('Que troço jóia!')



***Condição simplificada:***

Para situações mais simplificadas, onde haja apenas uma variável, pode se usar uma versão mais
resumida do comando, da seguinte forma:

t = int(input('Qual a idade do seu carro? '))
print('Que troço jóia!'if t <= 3 else 'Que troço brabo! tá na hora de vender isso aí, cariado!')
"""
'''Exercícios práticos'''

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2)/2
if m > 6:
    print('A sua média foi {:.2f}. Parabéns, você foi aprovado!'.format(m))
else:
    print('A sua média foi {:.2f}. Que pena, você errou... Volte para o seu lugar!'.format(m))