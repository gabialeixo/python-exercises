'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = col = maior = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = (int(input(f'Digite um valor para [{linha}, {coluna}]: ')))
print('-' * 50)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
    print()

print('-' * 50)
print(f'A soma dos números pares é {par}.')
for linha in range(0,3):
    col += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {col}.')
for c in range(0,3):
    if c == maior:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c] 
print(f'O maior valor da segunda linha é {maior}.')
print('{:=^40}'.format(' FIM DO PROGRAMA '))