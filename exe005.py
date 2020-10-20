#Faça um programa que leia um número inteiro e mostre na tela do seu sucessor e seu antecessor.

n = int(input('Digite um número inteiro: '))
ant = n - 1
suc = n + 1
print('O número antecessor é {} e seu sucessor é {}!'.format(ant, suc))