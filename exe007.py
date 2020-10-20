#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2
print('Nota 01: {}. \nNota 02: {}. \nMédia Final: {:.1f}.'.format(n1, n2, media))