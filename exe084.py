'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) quantas pessoas foram cadastradas.
B) uma listagem com as pessoas mais pesadas.
C) uma listagem com as pessoas mais leves.'''

dados = list()
listagem = list()
contagem = maior = menor = 0


while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite o seu peso: ')))
    contagem += 1
    if len(listagem) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    listagem.append(dados[:])
    dados.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

print('-' * 30)
print(f'{contagem} pessoas foram cadastradas.') #pode ser mostrado com (len(listagem)) no lugar de contagem.
print(f'A pessoa mais pesada tem {maior:.1f}kg e se chama ', end='')
for pessoa in listagem:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end='')
print()
print(f'A pessoa mais leve tem {menor:.1f}kg e se chama ', end='')
for pessoa in listagem:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end='')
print()
print('{:=^40}'.format(' FIM DO PROGRAMA '))
