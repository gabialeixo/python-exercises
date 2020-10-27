#Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
#digitado for ímpar, desconsidere-o.

soma = 0

for c in range(0,7):
    if c % 2 == 0:
        soma += c
print('A soma dos pares é {}.'.format(soma))
print('FIM.')