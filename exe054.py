#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
contador_maior = 0
contador_menor = 0

for c in range(0, 7):
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        contador_maior += +1
    else:
        contador_menor += +1

print('{} pessoas atingiram a maioridade! E {} ainda são de menor!'.format(contador_maior, contador_menor))
