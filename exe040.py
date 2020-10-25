#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando a mensagem no final de acordo com a média
#atingida.
#Média abaixo de 5.0: REPROVADO / entre 5.0 e 6.9: RECUPERAÇÃO / igual ou superior 7.0: APROVADO!

print('=' * 40)
print('SISTEMA DE NOTAS - COLÉGIO BUNO BOLTING')
print('=' * 40)

nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
media = (nota01 + nota02) / 2

if media <= 4.9:
    print('Você foi REPROVADO! Sua média final foi {:.1f}.'.format(media))
elif media >= 5.0 and media <=6.9:
    print('Você está em RECUPERAÇÃO! Sua média final foi {:.1f}.'.format(media))
elif media >= 7.0:
    print('Você foi APROVADO!! Sua média final foi {:.1f}.'.format(media))