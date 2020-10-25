#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto / à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal / 3x ou mais no cartão: 20% de juros.

print('=' * 18)
print('BOUTIQUE PIRILAMPO')
print('=' * 18)

produto = float(input('Valor do produto: '))

print(""" FORMAS DE PAGAMENTO
1 - À VISTA DINHEIRO/CHEQUE
2 - À VISTA CARTÃO DE CRÉDITO/DÉBITO
3 - 2X NO CARTÃO DE CRÉDITO
4 - 3X OU MAIS NO CARTÃO DE CRÉDITO
""")

pagamento = int(input('Digite a opção de pagamento que deseja: '))
if pagamento == 1:
    total = produto - (produto * 0.10)
    print('O valor à vista em dinheiro/cheque ficou R${:.2f}. Você recebeu 10% de desconto.'.format(total))
elif pagamento == 2:
    total = produto - (produto * 0.05)
    print('O valor à vista no cartão ficou R${:.2f}. Você recebeu 5% de desconto.'.format(total))
elif pagamento == 3:
    parcela = produto / 2
    print('O valor do produto em 2x permanece o mesmo R${:.2f}. O valor de cada parcela é R${:.2f}.'.format(produto, parcela))
elif pagamento == 4:
    parcela = int(input('Em quantas vezes você deseja parcelar: '))
    juros = (produto * 0.20) + produto
    total = juros / parcela
    print('O valor do produto parcelado em {}x foi para R${:.2f}. O valor de cada parcela é R${:.2f}.'.format(parcela, juros, total))

print('Obrigada pela preferência! Volte sempre!')