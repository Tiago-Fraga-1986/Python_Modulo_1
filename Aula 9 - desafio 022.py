# Desafio 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas minúsculas;
# Quantas letras ao todo (sem considerar espaços);
# Quantas letras tem o primeiro nome.
f = input('informe seu nome completo: ').strip()  # O ".strip()" vai eliminar qualquer espaço acidental inserido pelo
                                                  # user.
f1 = f.replace(' ', '')
pn = f.split()
print('Seu nome possui as seguintes características: ')
print('Com todas as letras maiúsculas ele fica {}'.format(f.upper()))
print('Com todas as letras minúsculas ele fica {}'.format(f.lower()))
print('Seu nome tem {} letras'.format(len(f1))) # é possível também fazer da seguinte forma: .format(len(f) -
                                                # f.count(' ')))
print('seu primeiro nome tem {} letras.'.format(len(pn[0])))
