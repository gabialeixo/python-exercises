#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite um número em metros: '))
cm = metros * 100
mm = metros * 1000
print('{} centímetros. {} milímetros.'.format(cm, mm))