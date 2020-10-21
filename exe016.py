#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math
num = float(input('Digite qualquer número aleatório e com vírgula: '))
conta = math.floor(num)
print('O número foi arredondado para baixo e sua porção inteira ficou: {}!'.format(conta))