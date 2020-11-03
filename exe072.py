#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Inválido. Tente novamente. ', end= '')
print(f'Você digitou o número {extenso[num]}.')

print('-' * 40)
print('{:=^40}'. format(' FIM DO PROGRAMA! '))
print('-' * 40)

