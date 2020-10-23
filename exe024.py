#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome o "SANTO"

cidade = input('Digite o nome da sua cidade: ')
div = cidade.split()
print('Santo' in div[0])