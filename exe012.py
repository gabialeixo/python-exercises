#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Valor do produto: '))
desconto = preco * 0.05
total = preco - desconto
print('O valor no produto na liquidação é {:.2f}!'.format(total))