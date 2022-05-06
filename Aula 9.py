"""
                                Aula 9 - Manipulando textos:
Cada String começa no "0" e vai até o final da ultima letra, contando os espaços.

Ex,: 
        f='Herr Comandant'
           0123456789...13 - Neste caso, a frase "Herr Comandant" possui 14 caracteres,
indo do "0" ao "13". Para todos os exemplos a seguir, usaremos essa frase para análise.

                                Regras de Fatiamento:
***Comandos:***

print(f([9])) ---> Mostrará o caracter que está na posição 9, no caso, o "n" .

print(f([5:13]) ---> Mostrará os caracteres da posição 5 até a 12, no caso, "Comandan".
Obs.: O fatiamento por range não considera a última posição informada, apresentando o
resultado até uma posição antes. Se o objetivo do comando fosse apresentar o resultado
"Comandant", o correto seria fazer da seguinte forma:

        print(f([5:14])

Note que não existe a posição "14" na frase, contudo, o python entenderá que deverá apresentar
todos os caracteres até o final.

print(f([5:14:2]) ---> Retornará da posição 5 a 13, pulando a cada duas posições. Deste
modo, o retorno será "Cmnat"

print(f([:4]) ---> Retorna da primeira posição até a informada. No caso, "Herr".

print(f([5:]) ---> Seguindo a lógica do anterior, o comando retornará da posição informada
até o final da frase. No caso, será "Comandant".

Print(f([5::2) ---> retornará da posição informada até o final da frase pulando a cada duas
posições. No caso, será "Cmnat".



***Análise***

print(len(f)) ---> mostra o "comprimento" da string. Neste caso, a resposta será "14"

print(f.count('n')) ---> Informa quantas vezes a letra informada entre ' ' aparece. Neste caso,
a resposta será "2".
Obs.: O Python é case sensitive, por isso, caso haja um "N", ele não contará.

print(f.count('n', 0, 10) ---> Contagem de quantos caracteres especificados entre '' existem
naquele intervalo. Neste caso, a resposta será "1".

print(f.find('dan') ---> Retorna a primeira posição onde se inicia a sequencia informada
entre ''. Neste caso, a resposta será "10"
Obs.: Caso seja inserida uma condição que não existe na frase, o programa retornará "-1".

print('Herr' in ((f)) ---> Informa se a palavra informada entre '' existe na frase. Neste caso,
a resposta será "True".



***Transformação***

print(f.replace('Herr', 'Senor')) ---> Substitui o conjunto de caracteres informado pelo segundo
conjunto informado. Neste caso, a resposta será "Senor Comandant".

print(f.upper()) ---> Colocará a frase inteira em maiúsculas. Neste caso, a resposta será
"HERR COMANDANT"

print(f.lower()) ---> Seguindo a lógica do anterior, o comando colocará a frase toda em minúsculas
Neste caso, a resposta será "herr comandant".

print(f.capitalize()) ---> Colocará apenas o primeiro caractere da frase em maiúsculas. Neste
caso, a resposta será "Herr comandant".

print(f.title()) ---> colocará a primeira letra de cada palavra em maiúsculas. Neste caso,
a resposta será "Herr Comandant".

f.strip() ---> Este é um módulo, não uma condição. Por isso, ele não pode ser "printado".
Este módulo elimina eventuais espaços à frente e ao final da frase digitada.

f.rstrip() ---> Removerá todos os espaços ao final da frase.

f.lstrip() ---> Removerá todos os espaços à frente da frase.



***Divisão***

f.split() ---> Localiza os espaços e segrega as palavras dentro de uma lista. Neste caso,
o retorno seria 'Herr Comandant' ---> ['Herr', 'Comandant']


***Junção***
'_'.join(f) ---> eliminará a lista, unindo os elementos com a separação informada entre ''.
Neste caso, o retorno seria ['Herr', 'Comandant'] ---> 'Herr_Comandant'.

"""