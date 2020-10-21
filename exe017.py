#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
#mostre o comprimento da hipotenusa.

import math
catop = float(input('Comprimento do cateto oposto: '))
catetoad = float(input('Comprimento do cateto adjacente: '))
hipo = math.hypot(catop, catetoad)
print('O resultado do comprimento da hipotenusa é: {:.2f}!'.format(hipo))