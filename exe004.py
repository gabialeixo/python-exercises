#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.

#string-str() #inteiro-int() #float-float() #boolean-bool()
x=input('Digite algo: ')
print('A tipo primitivo desse valor é:', type(x))
print('É alfanumérico? ', x.isalnum())
print('É somente alfabético? ', x.isalpha())
print('É decimal? ', x.isdecimal())
print('É um dígito? ', x.isdigit())
print('Está apenas com letras minúsculas? ', x.islower())
print('Está apenas com letras maiúsculas? ', x.isupper())
print('É numérico? ', x.isnumeric())
print('Só tem espaços? ', x.isspace())
print('Está capitalizada? ', x.istitle())