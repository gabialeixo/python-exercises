#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$1.00 =  R$3.27

din = float(input('Qaunto dinheiro você tem na carteira: '))
dol = din / 5.59
print('Tenho {:.2f} reais, que equivalem a {:.2f} dólares!'.format(din, dol))