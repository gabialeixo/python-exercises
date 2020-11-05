#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
#apenas os valores pares e os valores ímpares digitados respectivamente. No final mostre o conteúdo das três listas geradas.

numeros = list()
par = list()
impar = list()
contador = 0

while True:
    numeros.append(int(input('Digite um número: ')))
    contador += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

for c, valor in enumerate(numeros):
    if valor % 2 == 0:
        par.append(valor)
    elif valor % 2 == 1:
        impar.append(valor)


print('-' * 30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
print('{:=^40}'.format(' FIM DO PROGRAMA '))