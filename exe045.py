#Crie um programa que faça o computador jogar JOKENPÔ com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
jogada = randint(0, 2)

print('=' * 21)
print('JOKENPÔ COM A MÁQUINA')
print('=' * 21)

print("""VAMOS JOGAR!
0 - PEDRA
1 - PAPEL
2 - TESOURA
""")


escolha = int(input('Escolha a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)

print('Computador: {}'.format(itens[jogada]))
print('Sua jogada: {}'.format(itens[escolha]))

if jogada == 0:
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('COMPUTADOR VENCEU!')
    elif escolha == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA.')
elif jogada == 1:
    if escolha == 0:
        print('COMPUTADOR VENCEU!')
    elif escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA.')
elif jogada == 2:
    if escolha == 0:
        print('VOCÊ VENCEU!')
    elif escolha == 1:
        print('COMPUTADOR VENCEU!')
    elif escolha == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA.')

