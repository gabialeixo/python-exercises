#Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Digite um número para saber o seu fatorial: '))
fatorial = 1

while num > 1:
    fatorial *= num
    num -= 1

print('O fatorial é {}.'.format(fatorial))