'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total de gasto na compra.
B) Quantos produtos custam mais de R$1000,00.
C) Qual é o nome do produto mais barato.'''

print('-' * 17)
print('LOJÃO DA ECONOMIA')
print('-' * 17)

total = contador = caro = menor = 0
barato = ''

while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço do produto: R$'))
    contador += 1
    total += preco
    if preco >= 1000:
        caro += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar a compra? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-' * 50)
print(f'O valor total da sua compra foi R${total:.2f}.')
print(f'{caro} produtos custam mais de R$1000,00.')
print(f'O produto mais barato da sua compra foi {barato} e custou R${menor:.2f}')
print('\n{:=^40}'.format(' VOLTE SEMPRE '))