""" Desafio 33 - Faça um programa que leia três números e mostre qual é o maior
e qual é o menor."""
pv = int(input('digite o primeiro valor: '))
sv = int(input('digite o segundo valor: '))
tv = int(input('digite o terceiro valor: '))
men = pv
if sv < pv and sv < tv:
    men = sv
if tv < pv and tv < sv:
    men = tv
mai = pv
if sv > pv and sv > tv:
    mai = sv
if tv > pv and tv > sv:
    mai = tv
print('o menor valor é {} e o maior é {}'.format(men, mai))
