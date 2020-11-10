#Aprimore o DESAFIO093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de
#aproveitamento de cada jogador.

dados = list()
futebol = dict()
gols = list()
soma_gols = 0

while True:
    futebol.clear()
    futebol['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {futebol["nome"]} jogou: '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'    Quantos gols na partida {c+1}: ')))
    futebol['gols'] = gols[:]
    futebol['total'] = sum(gols)
    dados.append(futebol.copy())
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-' * 50)
print('{:<5}{:<20}{:^5}{:>20}'.format('COD','Nome','Gols', 'Total'))
print('-' * 50)
for i, a in enumerate(dados):
    print(f'{i:<5}', end= '')
    for d in a.values():
        print(f'{str(d):<20}', end='')
    print()

while True:
    print('-' * 50)
    info_geral = int(input('Mostrar dados de qual jogar? (999 para interromper) '))
    if info_geral == 999:
        break
    if info_geral >= len(dados):
        print(f'ERRO! Não existe jogador com o código {info_geral}!!!')
    else:
        print(f'=> LEVANTAMENTO DO JOGADOR {dados[info_geral]["nome"]}: ')
        for c, v in enumerate(dados[info_geral]['gols']):
            print(f'    => Na partida {c+1} fez: {v} gols.') 
    print('-' * 50)
print('{:=^50}'.format(' PROGRAMA ENCERRADO '))