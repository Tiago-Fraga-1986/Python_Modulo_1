# Desafio 024 - Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com "Santo".
c = str(input('Informe o nome de sua cidade: ')).strip().lower().split()
s = 'santo' in c[0]
print('O primeiro nome da sua cidade é "Santo"? {}'.format(s))
