'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

numeros = list()
contador = 0

while True:
    numeros.append(int(input('Digite um número: ')))
    contador += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-' * 30)
print(f'Você digitou {contador} números.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O número 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
print('{:=^40}'.format(' FIM DO PROGRAMA '))
