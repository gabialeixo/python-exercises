#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão aritimética. No final, mostre os 10 primeiros
#termos dessa progressão.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
progressao = termo + (10 - 1) * razao

for c in range(termo, progressao + razao, razao):
    print('{}'.format(c), end=' -> ')
print('FIM.')