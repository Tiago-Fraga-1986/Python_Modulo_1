""" Desafio 007 - Desenvolva um programa que leia as notas de um aluno e informe a média deste."""
n = input('Nome do Aluno: ')
n1 = float(input('Nota do primeiro semestre: '))
n2 = float(input('Nota do segundo semestre:'))
m = (n1+n2)/2
print('O aluno {} obteve nota {:.2f} no primeiro semestre e {:.2f} no segundo semestre. A média do aluno é {:.2f}'
      .format(n, n1, n2, m))
