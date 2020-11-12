#Faça um programa que tenha um função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem
#que analisar todos os valores e dizer qual deles é maior.

from time import sleep

def linha():
    print('-' * 30)


def maior(* num):
    print('Analisando os valores passados...')
    sleep(1)
    tam = len(num)
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
    print(f'Foram analisados {tam} valores ao todo.')
    mai = max(num)
    print(f'O maior valor informado foi {mai}.')
print('FIM!')

linha()
maior(3, 4, 5, 2, 8, 9)
linha()
maior(3, 5, 2)
linha()
maior(0)
linha()
maior(1)
linha()