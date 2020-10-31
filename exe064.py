#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
#999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles.
#(Desconsiderando o flag).

num = contador = soma = 0
num = int(input('Digite um número inteiro (999 caso queira parar): '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número inteiro (999 caso queira parar): '))
print('Você digitou {} números e a soma entre eles é {}.'.format(contador, soma))