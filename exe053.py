#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
verificacao = frase.split()
fraseinteira = ''.join(verificacao)
contrario = ''

for c in range(len(fraseinteira) -1, -1, -1):
    contrario += fraseinteira[c]
if contrario == fraseinteira:
    print('É UM POLÍNDROMO! Sua frase: {}. Frase ao contrário: {}.'.format(frase, contrario))
else:
    print('NÃO É UM POLÍNDROMO! Sua frase: {}. Frase ao contrário: {}.'.format(frase, contrario))
