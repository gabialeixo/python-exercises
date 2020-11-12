#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai
#sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares
#sorteados pela função anterior.

from random import randint
from time import sleep


def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        c = randint(1, 10)
        lista.append(c)
        print(f'{c} ', end='')
        sleep(0.5)
    print('PRONTO!')
    sleep(1)


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}.')


numeros = list()
sorteio(numeros)
somaPar(numeros)