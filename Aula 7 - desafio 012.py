"""Desafio 012 - receba o valor de um produto e o desconto, calculando e apresentando o valor com o desconto. """
r = float(input('Qual o preço do produto? R$ '))
d = float(input('Qual será o desconto aplicado? '))
desc = r*(d/100)
prc = r-desc
print('Este produto, com o desconto de {}%, fica por R${:.2f}'.format(d, prc))
