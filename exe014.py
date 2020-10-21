#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Quantos graus está agora? '))
fah = (temp * 1.8) + 32
print('A temperatura em Fahrenheit está: {:.1f}!'.format(fah))