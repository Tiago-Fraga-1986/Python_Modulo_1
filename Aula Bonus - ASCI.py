"""Aula 11 - Cores no terminal:
O Python pode usar, dentro do seu código, a linguagem asci para colorir frases ou palavras.
o código base para inserir cores no terminal é o seguinte:

\033[0;33;44m

sendo:

\033 - o recurso usado (é o comando que chama a colorização);
[ - o comando que informa o inicio da estilização
0 - o estilo. No Python, os estilos que funcionam é o 0 (sem estilo), 1(bold), 4(underline)
    e 7(negative).
33 - opção de cor da fonte. Os códigos de cor variam do 30 ao 37 e são, respectivamente: Branco,
     vermelho, verde, amarelo, azul, roxo, azul claro e cinza.
44 - Opção de cor do fundo. Os códigos variam de 40 a 47 e são, respectivamente: Branco, vermelho,
     verde, amarelo, azul, roxo, azul claro e cinza.


Para aplicar a cor. basta inserir esse padrão antes da palavra pretendida. por exemplo:

print('\033[1;34;44m teste\033[m')

Para interromper a cor, basta inserir "\033[m" ao final da frase. Isso vai indicar o fim do comando.

Obs.: O comando de inicio e de final da cor ficam DENTRO das aspas da str.

#Exemplos práticos:

n1 = float(input('Digite a nota do primeiro semestre: '))
n2 = float(input('Digite a note do segundo semestre: '))
m = (n1 + n2) / 2
if m < 6:
    print('\033[97mSua média final é\033[m \033[1;31m{:.2f}\033[m \033[97me você foi\033[m \033[1;31mReprovado.\033[m'
    .format(m))
else:
    print('\033[97mSua média final é\033[m \033[1;32m,{:.2f} \033[m \033[97me você foi \033[1;32mAprovado! \033[m'
    .format(m))

"""
# Usando o exemplo anterior como base, existe uma forma mais organizada de como montar a estrutura de cores. para
# isso, monta-se um "dicionário" com as cores e seus respectivos códigos, bem como um comando "limpa". isso será
# colocado no ".format", do seguinte modo:

n1 = float(input('Informe a nota do primeiro semestre: '))
n2 = float(input('Informe a nota do segundo semestre: '))
m = (n1 + n2) / 2
cor = {'lp': '\033[m', 'vm': '\033[1;31m', 'vd': '\033[1;32m', 'br': '\033[97m'}
if m < 6:
    print('{}Sua média final é {}{}{:.2f}{}{} e você foi {}{}Reprovado.'.format(
        cor['br'], cor['lp'], cor['vm'], m, cor['lp'], cor['br'], cor['lp'], cor['vm']))
else:
    print('{}Sua média final é {}{}{:.2f}{}{} e você foi {}{}Aprovado!'.format(
        cor['br'], cor['lp'], cor['vd'], m, cor['lp'], cor['br'], cor['lp'], cor['vd']))
