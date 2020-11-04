#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e menor valor
#digitado e suas respectivas posições na lista.

valores = list()


for c in range(1,6):
    valores.append(int(input(f'Digite um valor para posição {c}: ')))

maior = max(valores)
menor = min(valores)

print(f'\nVocê digitou os valores: {valores}.')
print(f'\nO maior valor digitado foi {maior} nas posições ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c+1}', end='...')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c+1}', end='...')
print()
        
print('\n{:=^40}'.format(' FIM DO PROGRAMA '))