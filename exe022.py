#Crie um programa que leia um nome completo de uma pessoa e mostre:
#O nome com todas as letras minúsculas
#O nome com todas as letras maiúsculas
#Quantas letras tem ao todos(sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')
minu = nome.lower()
maiu = nome.upper()
todo = nome.replace(" ", "")
letras = nome.split()
print(minu)
print(maiu)
print('Seu nome tem {} letras!'.format(len(todo)))
print('Seu primeiro nome tem {} letras!'.format(len(letras[0])))