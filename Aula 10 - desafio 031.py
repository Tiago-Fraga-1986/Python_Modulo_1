""" Desafio 31 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule
o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens
mais longas."""
d = float(input('Qual a distância da sua viagem? '))
if d > 200:
    print('O valor da sua passagem ficou estabelecido em R$ {:.2f}.'.format(d * 0.45))
else:
    print('O valor da sua passagem ficou estabelecido em R$ {:.2f}.'.format(d * 0.50))
