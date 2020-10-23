#Faça um programa que leia um nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip()
div = nome.split()
print('Primeiro nome: {}.'.format(div[0]))
print('Último nome: {}.'.format(div[len(div)-1]))