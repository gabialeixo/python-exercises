#Crie um programa que leia um número inteiro qualquer e mostre se ele é PAR ou ÍMPAR

num = int(input('Digite um número inteiro qualquer: '))
if num % 2 == 0:
    print('Seu número {} é PAR!'.format(num))
else:
    print('Seu número {} é ÍMPAR!'.format(num))