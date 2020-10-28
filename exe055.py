#Faça um programa que leia o peso de 5 pessoas e no final mostre qual foi o maior e o menor peso lidos.

contador_maior = 0
contador_menor = 1000

for c in range(0, 5):
    peso = float(input('Digite o seu peso atual: '))
    if peso >= contador_maior:
        contador_maior = peso
    if peso <= contador_menor:
        contador_menor = peso

print('O menor peso da lista é {}. O maior peso da lista é {}.'.format(contador_menor, contador_maior))