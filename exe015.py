#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias 
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos km você percorreu? '))
dias = int(input('Quantos dias você utilizou o carro? '))
kmrodado = km * 0.15
diasrodado = dias * 60
total = kmrodado + diasrodado
print('Você rodou {}KM e deu um valor de: R${:.2f} e a quantidade de dias foi {} e a pagar é: R${}.'.format(km, kmrodado, dias, diasrodado))
print('O total geral a pagar é: R${}.'.format(total))