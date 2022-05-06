"""Desafio 015 - Faça uma calculadora de aluguel de veículos que considere:
* O período (em dias) de aluguel do veículo;
* A quilometragem percorrida no período.
O programa deve retornar o valor em R$ a ser pago, considerando o aluguel de R$60/dia e R$015 por Km rodado."""
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km você rodou no período? '))
valor = dias * 60 + km * 0.15
print('O total do aluguel do veículo ficou em R${:.2f}.'.format(valor))
