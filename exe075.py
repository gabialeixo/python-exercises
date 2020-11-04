'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))
num4 = int(input('Digite outro número: '))

numeros = (num1, num2, num3, num4)

print('-' * 15)
print(f'Você digitou os valores {numeros}.')
print('-' * 15)
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
print('-' * 15)
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3)+1}º posição.')
else:
    print('O número 3 não foi digitado em nenhuma posição!')
print('-' * 15)
print('Os números pares digitados foram: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
print('\n{:=^40}'.format(' FIM DO PROGRAMA '))