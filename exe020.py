#O mesmo professor do desafio anterior, quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem do sorteado.

import random
alu01 = input('Aluno 01: ')
alu02 = input('Aluno 02: ')
alu03 = input('Aluno 03: ')
alu04 = input('Aluno 04: ')
ordem = [alu01, alu02, alu03, alu04]
random.shuffle(ordem)
print('A ordem de apresentação será: {}'.format(ordem))