"""Desafio 011 - Crie um programa que receba a altura e a largura de uma parede. O programa deve informar:
* A área;
* Quanto de tinta será usado para efetuar a pintura (Considere que, para pintar 2m², usa-se 1l de tinta."""

alt = float(input('Qual a altura da parede (em "m"): '))
lrg = float(input('Qual a largura da parede (em "m"): '))
area = alt*lrg
tnt = area/2
print('A área de sua parede é {:.2f}m². Para este espaço, você precisará de {:.2f}l de tinta.'.format(area, tnt))
