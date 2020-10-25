#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar
#o valor da casa -  o salário do comprador - e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('-' * 20)
print('BEM-VINDO(A) AO BANCO TUTTI-FRUTTI')
print('-' * 20)

print("""
0 - SALDO
1 - EXTRATO
2 - EMPRÉSTIMOS
3 - SAIR
""")
opcao = int(input('Por favor, digite a opção que você deseja: '))
if opcao == 0 or opcao == 1:
    print('Serviço indisponível no momento! Tente mais tarde!')
elif opcao == 2:
    print('Bem-Vindo(a) a área de Empréstimos. Preciso de algumas informações!')
    valorcasa = float(input('Qual o valor da casa desejada? '))
    salario = float(input('Qual o valor do seu salário atual? '))
    tempo = int(input('Em quantos meses deseja pagar esse imóvel? '))
    parcela = valorcasa / tempo
    verificacao = (salario * 0.30)
    if parcela < verificacao:
        print('PARABÉNS! Seu empréstimo foi aprovado e o valor da sua parcela será de R${:.2f} por {} meses.'.format(parcela, tempo))
    else:
        print('Valor da parcela: R${:.2f}.'.format(parcela))
        print('Infelizmente a parcela do empréstimo excedeu 30% do seu salário R${:.2f}! Empréstimo negado!'.format(verificacao))
elif opcao == 3:
    print('Obrigado por utilizar nossos serviços! Desejamos um ótimo dia!')