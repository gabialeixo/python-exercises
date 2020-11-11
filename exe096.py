#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(altura e comprimento)
#e mostre a área do terreno.

def linha():
    print('-' * 30)

def area(a, b):
    total = a * b
    print('-' * 30)
    print(f'A área de um terreno {a} x {b} é de {total}m².')


linha()
print('{:^30}'.format('CONTROLE DE TERRENO'))
linha()
area(a = float(input('LARGURA(m): ')), b = float(input('COMPRIMENTO(m): ')))

    
