#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro qualquer: '))
primo = 0

for c in range(1, num+1):
    if num % c == 0:
        primo += + 1
if primo == 2:
    print('O número digitado é PRIMO!')
else:
    print('O número digitado NÃO É PRIMO!')