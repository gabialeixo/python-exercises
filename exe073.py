'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time do Vasco.'''

from time import sleep

times = ('Internacional', 'Flamengo', 'Atlético-MG', 'Fluminense', 'São Paulo', 'Santos', 'Palmeiras', 'Grêmio'
          'Sport Recife', 'Fortaleza', 'Corinthians', 'Ceará SC', 'Atlético-GO', 'Botafogo', 'Bahia', 'Vasco da Gama',
          'Coritiba', 'Bragantino-SP', 'Athletico-PR', 'Goiás')

print('-' * 21)
print('TABELA DO BRASILEIRÃO')
print('-' * 21)

opcao = 0

while opcao != 5:
    print(''' === MENU ===
    [1] 5 Primeiros times
    [2] Zona de Rebaixamento
    [3] Times Ordem Alfabética
    [4] Vasco da Gama
    [5] Sair''')
    opcao = int(input('O que deseja procurar? '))
    if opcao == 1:
        print(f'Os 5 primeiros times são: {times[0:5]}')
        print('-' * 30)
    sleep(1)
    if opcao == 2:
        print(f'Zona de rebaixamento: {times[15:20]}')
        print('-' * 30)
    sleep(1)
    if opcao == 3:
        print('Ordem alfabética:')
        print(sorted(times))
        print('-' * 30)
    sleep(1)
    if opcao == 4:
        print(f'O Vasco da Gama está na {times.index("Vasco da Gama")+2}º posição.')
    sleep(1)
    if opcao == 5:
        print('{:=^40}'.format(' FIM DA TABELA '))