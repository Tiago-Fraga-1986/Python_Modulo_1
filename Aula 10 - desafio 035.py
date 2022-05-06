"""Desafio 35 - Desenvolva um programa que leia o comprimento de três retas e diga ao
usuário se elas podem ou não formar um triangulo."""
print('∆'*20)
print('ANALISADOR DE TRIANGULOS')
print('∆'*20)
s1 = float(input('informe o primeiro segmento: '))
s2 = float(input('informe o segundo segmento: '))
s3 = float(input('informe o terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos informados FORMAM um triangulo.')
else:
    print('Os segmentos informados NÃO FORMAM um triangulo')