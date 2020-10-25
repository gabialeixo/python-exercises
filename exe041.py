#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#categoria, de acordo com a idade:
#até 9 anos: mirim / até 14 anos: infantil / até 19: júnior / até 20 anos: sênior / acima: master.

from datetime import date

print('=' * 32)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('=' * 32)

nascimento = int(input('Digite o ano de seu nascimento: '))
ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print('Você tem {} anos. Sua categoria é MIRIM!'.format(idade))
elif idade >= 10 and idade <= 14:
    print('Você tem {} anos. Sua categoria é INFANTIL!'.format(idade))
elif idade >= 15 and idade <= 19:
    print('Você tem {} anos. Sua categoria é JÚNIOR!'.format(idade))
elif idade == 20:
    print('Você tem {} anos. Sua categoria é SÊNIOR!'.format(idade))
elif idade >= 21:
    print('Você tem {} anos. Sua categoria é MASTER!'.format(idade))