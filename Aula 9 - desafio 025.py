# Desafio 025 - Crie um programa que leia o nome de uma pessoa e
# diga se ela tem "Silva" no nome:
n = str(input('Informe o seu nome completo: ')).strip()
print('Seu nome possui "Silva"? {}'.format('silva' in n.lower()))
