#Crie um programa onde o usuário possa digitar vários valores numérios e cadastre-os em uma lista. Caso o número já exista
#lá dentro, ele não será adicionado. No final serão exibidos todos os valores únicos digitados em ordem crescente.

print('-' * 20)
print('{:^20}'.format('CADASTRAMENTO'))
print('-' * 20)

valores = list()

while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não pode ser adicionado novamente.')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-' * 30)
valores.sort()
print(f'Os valores adicionados foram {valores}.')
print('{:=^40}'.format(' FIM DO PROGRAMA '))
