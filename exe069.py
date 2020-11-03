'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
o usuário quer ou não continuar. No final mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''

print('=' * 20)
print('CADASTRAMENTO SOCIAL')
print('=' * 20)

idade = contador = homem = mulher = 0

while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        contador += 1
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
        if sexo == 'M':
            homem += 1
        if sexo == 'F':
            if idade < 20:
                mulher += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-' * 30)
print(f'{contador} pessoas são maiores de 18 anos.')
print(f'Foram cadastrados {homem} homens.')
print(f'Tem {mulher} mulheres com menos de 20 anos.')
print('\n=========== FIM DO PROGRAMA ===========')
