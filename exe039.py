#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar. Se é hora de ser alistar. Ou se já passou do tempo do alistamento.
#O programa também deve apresentar o tempo que falta ou que passou do prazo.

from datetime import date
print('=' * 20)
print('BEM VINDO AO ALISTAR')
print('=' * 20)

alistar = date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
idade = alistar - ano

if idade < 17:
    print('Ainda não está na hora do seu alistamento! Faltam {} anos.'.format(18 - idade))
elif idade > 18:
    print('Já passou {} anos do seu alistamento!! Está na hora de resolver esse assunto!'.format(idade - 18))
else:
    print('Corra! Está na hora de se alistar!!')

