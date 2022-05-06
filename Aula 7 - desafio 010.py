"""Desafio 010 - Crie um conversor de moedas que leia o valor em Reais (R$) e retorne a cotação em Dólar (U$) e Euros
(EU$). Considerou-se uma cotação fixa das moedas de R$4.69 - U$1.00 e R$5.70 - EU$1.00"""
n = input('Qual o seu nome? ')
r = float(input('Quantos Reais você tem? R$'))
us = float(r/4.69)
eu = float(r/5.70)
print('{}, Com o investimento de R${:.2f} você consegue comprar U${:.2f} ou Eu${:.2f}.'.format(n, r, us, eu))
