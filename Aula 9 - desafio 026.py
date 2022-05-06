# Desafio 026 - Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "a";
# Em qual posição ela aparece a primeira vez; Em que posição ela aparece a última vez.
f = str(input('escreva uma frase qualquer: ')).strip().lower()
print('A frase apresenta a letra "a" {} vezes, sendo que a primeira vez ela aparece '
      'na posição {} e a ultima vez na posição {}'
      .format(f.count('a'), f.find('a') + 1,
              f.rfind('a') + 1))  # O "+1" é necessário para adequar a contagem à palavra.
