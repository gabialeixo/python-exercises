#Crie um programa que vai gerar 5 números aleatórios e colocar eles em uma tupla. Depois disso mostre a listagem de números
#gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os números sorteados foram: ', end= '')
for c in aleatorio:
    print(f'{c} ', end= '')

print(f'\nO menor número é {min(aleatorio)} e o maior número é {max(aleatorio)}.')