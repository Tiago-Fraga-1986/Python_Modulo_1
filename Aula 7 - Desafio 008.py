# Desafio 008 - Crie um conversor de medidas que receba uma medida em metros e informe a mesma em Km, Cm e mm:
m = float(input('informe a medida em "m": '))
km = (float(m/1000))
cm = int(m*100)
mm = int(m*1000)
print('{:.2f}m são {:.2f}km, {}cm ou {}mm.'.format(m, km, cm, mm))
