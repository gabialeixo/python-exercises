#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
#e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = contador = soma = maior = menor = 0
resposta = 'S'

while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    contador += 1
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()
media = soma / contador
print('Você digitou {} números e a média de todos os valores digitados foi {}.'.format(contador, media))
print('O menor número foi {} e o maior foi {}.'.format(menor, maior))
print('Fim')