#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

sal = float(input('Qual o valor do seu salário atual? R$'))
aumento = sal * 0.15
total = sal + aumento
print('Você ganhou um aumento de R${:.2f} e passa a ganhar R${:.2f}'.format(aumento, total))