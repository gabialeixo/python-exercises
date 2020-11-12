#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from datetime import date

def voto(nasc):
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO!')
    if idade >=16 and idade < 18 or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    if idade >= 18 and idade <=64:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')


print('-' * 35)
voto(int(input('Qual seu ano de nascimento? ')))
