#Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
#digitado for ímpar, desconsidere-o.

soma = 0
contador = 0

for c in range(1,7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        contador += 1
print('Você digitou {} números PARES e a soma desses pares é {}.'.format(contador, soma))
print('FIM.')