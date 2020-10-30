'''Crie um programa que leia dois valores e mostre o menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

print('=' * 10)
print('CONTORANDO')
print('=' * 10)

num01 = float(input('Digite um valor: '))
num02 = float(input('Digite outro valor: '))
opcao = 0

while opcao != 5:
    opcao = int(input('''=== MENU ===
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa

    Digite a opção desejada: '''))

    if opcao == 1:
        soma = num01 + num02
        print('A soma do {} e {} é igual a {}.'.format(num01, num02, soma))
    sleep(0.5)
    if opcao == 2:
        multiplicacao = num01 * num02
        print('A multiplicação entre {} e {} é igual a {}.'.format(num01, num02, multiplicacao))
    sleep(0.5)
    if opcao == 3:
        if num01 == num02:
            print('Os números são iguais.')
        elif num01 > num02:
            print('O maior número é {}.'.format(num01))
        else:
            print('O maior número é {}.'.format(num02))
    sleep(0.5)
    if opcao == 4:
        num01 = int(input('Digite um novo valor: '))
        num02 = int(input('Digite um novo segundo valor: '))
    sleep(0.5)
    if opcao == 5:
        print('Já vai?! Que pena!')
print('Fim!')
