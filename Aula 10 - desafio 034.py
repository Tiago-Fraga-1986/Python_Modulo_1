"""Desafio 34 - Escreva um programa que pergunte o salário de um funcionário e
calcule o valor de seu aumento. Para salários superiores a R$1.250,00, calcule um aumento
de 10%. Para os inferiores ou iguais, o aumento é de 15%."""
n = str(input('Qual o seu nome? '))
n1 = n.strip().capitalize().split()
s = float(input('{}, informe o seu salário: R$ '.format(n1[0])))
s1 = (s * 0.1)
s2 = (s * 0.15)
if s >= 1250:
    print('{}, o reajuste do seu salário foi estabelecido em R$ {:.2f}. Seu novo salário será '
          'R$ {:.2f}.'. format(n1[0], s1, s1+s))
else:

    print('{}, o reajuste do seu salário ficou estabelecido em {:.2f}. Seu novo salário será'
          'R$ {:.2f}.'. format(n1[0], s2, s2 + s))
