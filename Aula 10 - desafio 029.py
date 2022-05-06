""" Desafio 29 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
 mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima
 do limite."""
v = float(input('Informe a velocidade do veículo: '))
m = (v-80)*7
if v <= 80:
    print('Você está dentro do limite de velocidade')
else:
    print('Você ultrapassou a velocidade limite. Sua multa foi estabelecida em R${:.2f}'.format(m))
