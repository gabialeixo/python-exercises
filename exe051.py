#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão aritimética. No final, mostre os 10 primeiros
#termos dessa progressão.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
progressao = termo
print(termo)

for c in range(0,9):
    progressao += razao
    print(progressao)