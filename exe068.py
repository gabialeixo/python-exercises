#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando
#o total de vitórias que ele conquistou no final do jogo.

from random import randint
from time import sleep
jogador = contador = 0


while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Você quer par ou ímpar? [P/I] ')).strip().upper()[0]
        sleep(1)
    print('Um... Dois... Três... e JÁ:')
    sleep(1)
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total deu {total}.')
    if escolha == 'P':
        if total % 2 == 0:
            print('DEU PAR! Você ganhou!')
            contador += 1
        else:
            print('DEU ÍMPAR! Você perdeu!')
            break
    elif escolha == 'I':
        if total % 2 == 0:
            print('DEU PAR! Você perdeu!')
            break
        else:
            print('DEU ÍMPAR! Você ganhou!')
            contador += 1
    print('Vamos jogar novamente...')
print('-' * 20)
print(f'ACABOU! Você conseguiu ganhar {contador} vezes!')
