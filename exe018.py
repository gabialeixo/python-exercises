#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite um ângulo qualquer: '))
sin = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O seno do seu ângulo é: {:.2f}, o cosseno é: {:.2f} e a tangente é {:.2f}: .'.format(sin, cos, tan))