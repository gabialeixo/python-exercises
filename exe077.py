#Crie um programa que tenha uma tupla com várias palavras(não utilize acentos). Depois disso, você deve mostrar para cada
#palavra, quais são suas vogais.

palavras = ('aluno', 'brilhante', 'diamante', 'silicone', 'caneta', 'caderno', 'agenda',
            'paralelepipedo', 'margarida', 'girassol')

print('-' * 30)
print('{:^30}'.format('JOGO DAS VOGAIS'))
print('-' * 30)


for c in palavras:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for vogais in c:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')

print('\n{:=^40}'.format(' FIM DO PROGRAMA '))