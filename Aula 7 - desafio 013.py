"""Desafio 013 - Programe um código que receba o salário de um funcionário e apresente o mesmo com 15% de aumento."""
n = str(input('Qual o seu nome? '))
n1 = n.strip().capitalize().split()
sal = float(input('{}, qual o seu salário? '.format(n1[0])))
aum = (sal * 0.15) + sal
print('{}, com o reajuste de 15%, seu salário irá de R${:.2f} para R${:.2f}.'.format(n1[0], sal, aum))
