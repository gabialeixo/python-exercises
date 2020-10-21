#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajuda ele lendo o nome
#delas e escrevendo o nome do escolhido.

import random
alu01 = input('Aluno 01: ')
alu02 = input('Aluno 02: ')
alu03 = input('Aluno 03: ')
alu04 = input('Aluno 04: ')
escolhido = random.choice([alu01, alu02, alu03, alu04])
print('O escolhido para apagar o quadro foi {}.'.format(escolhido))
