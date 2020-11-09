'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos
os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.'''

dados = list()
cadastro = dict()
contador = media = soma = 0

print('-' * 30)
print('{:^30}'.format(' CADASTRAMENTO '))
print('-' * 30)

while True:
    cadastro['nome'] = str(input('Nome: '))
    contador += 1
    while True:
        cadastro['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
        if cadastro['sexo'] in 'FM':
            break
        print('ERRO. Digite apenas F ou M.')
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    media = soma / contador
    dados.append(cadastro.copy())
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

print('-' * 50)
print(f'- O grupo tem {contador} pessoas.')
print(f'- A média de idade do grupo é de {media:.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for m in dados:
    if m['sexo'] == 'F':
        print(f'{m["nome"]} ', end='')
print()
print('- Lista das pessoas que estão acima da média: ') 
for p in dados:
    if p['idade'] >= media:
        print('    ', end='')
        for key, value in p.items():
            print(f'{key} = {value}; ', end='')
        print()

print('{:=^50}'.format(' FIM DO PROGRAMA '))