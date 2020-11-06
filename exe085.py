#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
#separado os valores. No final, mostre os valores pares e ímpares em ordem crescente.

valor = [[], []]
num = 0

for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        valor[0].append(num)
    else:
        valor[1].append(num)
    
print('-' * 30)
valor[0].sort()
valor[1].sort()
print(f'Os valores pares digitados foram {valor[0]}')
print(f'Os valores ímpares digitados foram {valor[1]}')
print('{:=^40}'.format(' FIM DO PROGRAMA '))