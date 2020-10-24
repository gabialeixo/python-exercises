#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles pode ou não formar um triângulo.

reta01 = float(input('Digite o comprimento da primeira reta: '))
reta02 = float(input('Digite o comprimento da segunda reta: '))
reta03 = float(input('Digite o comprimento da terceira reta: '))

if (reta01 < reta02 + reta03) and (reta02 < reta01 + reta03) and (reta03 < reta01 + reta02):
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')
