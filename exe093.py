#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa deve ler o nome do jogador e quantas
#partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso deverá ser guardado
#em um dicionário, incluindo o total de gols feitos durante o campeonato.

futebol = dict()
gols = list()
soma_gols = 0

futebol['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {futebol["nome"]} jogou: '))
for c in range(0, partidas):
    qtd = int(input(f'Quantos gols na partida {c+1}: '))
    soma_gols += qtd
    gols.append(qtd)
    futebol['gols'] = gols
    futebol['total'] = soma_gols
print('-' * 50)
print(futebol)
print('-' * 50)
for key, value in futebol.items():
    print(f'O campo {key} tem o valor {value}.')
print('-' * 50)
print(f'O jogador {futebol["nome"]} jogou {partidas} partidas.')
for c, v in enumerate(futebol['gols']):
    print(f'    => Na partida {c+1}, fez {v} gols.')
print(f'Foi um total de {futebol["total"]} gols.')