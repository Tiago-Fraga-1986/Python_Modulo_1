# Desafio 027 - Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
n = input('Informe o seu nome completo: ').strip().split()
print('primeiro nome: {}'.format(n[0]))
print('Último nome: {}'.format(n[-1]))
