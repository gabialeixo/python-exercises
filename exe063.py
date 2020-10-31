#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.


n = int(input('Digite um número inteiro qualquer: '))
termo = 0
fibonacci = 1
print('{} -> {}'.format(termo, fibonacci), end='')
contador = 3

while contador <= n:
    total = termo + fibonacci
    print(' -> {}'.format(total), end='')
    termo = fibonacci
    fibonacci = total
    contador += 1
print(' -> Fim.')