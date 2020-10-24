#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00 calcule um aumento de 10%.
#Para os inferiores ou iguais o aumento é de 15%.

salario = float(input('Qual é o seu salário atual? '))
if salario <= 1250:
    calculo2 = salario * 0.15
    aumento2 = salario + calculo2
    print('Seu aumento foi de R${:.2f} e seu salário agora é: R${:.2f}.'.format(calculo2, aumento2))
else:
    calculo = salario * 0.10
    aumento = salario + calculo
    print('Seu aumento foi de R${:.2f} e seu salário agora é: R${:.2f}.'.format(calculo, aumento))