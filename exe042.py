#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#equilátero: todos os lados iguais / isósceles: dois lados iguais / escaleno: todos os lados diferentes.

lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))

if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print('Esses valores formam um triângulo EQUILÁTERO!')
    elif (lado1 == lado2 and lado1 != lado3) or (lado1 == lado3 and lado1 != lado2) or (lado2 == lado3 and lado2 != lado1):
        print('Esses valores formam um triângulo ISÓSCELES!')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('Esses valores formam um triângulo ESCALENO!')
else:
    print('Esses valores não podem formar nenhum triângulo!')