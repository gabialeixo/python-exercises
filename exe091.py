#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador01': randint(1,6),
        'jogador02': randint(1,6),
        'jogador03': randint(1,6),
        'jogador04': randint(1,6)
        }

ranking = list()

print('Valores sorteados: ')
for key, value in jogo.items():
    print(f'O {key} tirou {value} no dado.')
    sleep(1)

print('-' * 30)
print('Ranking dos jogadores: ')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)