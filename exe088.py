#Faça um programa que ajude um jogador da mega-sena a criar palpites. O programa vai perguntar quantos jogos serão gerados
#e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from time import sleep
from random import randint

print('-' * 40)
print('{:^40}'.format(' PALPITES DA MEGA-SENA '))
print('-' * 40)

qtd = int(input('Quantos jogos quer gerar? '))
numeros = []

print('-' * 40)
for c in range(0, qtd):
    numeros.append(list())
    for n in range(0, 6):
        sorteio = randint(0, 61)
        numeros[c].append(sorteio)
    print(f'Jogo {c+1}: {sorted(numeros[c])}', end='\n')
    sleep(1)
print()

print('{:=^40}'.format(' : BOA SORTE : '))
