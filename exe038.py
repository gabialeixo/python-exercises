#Escreve um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior. Ou o segundo valor é maior. Ou não existe valor maior, os dois são iguais.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print('O primeiro valor é maior!')
elif num2 > num1:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois valores são iguais!')
