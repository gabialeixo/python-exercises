#Crie um programa que leia nome e duas notas de vários alunos e guarde em uma lista composta. No final, mostre um boletim
#contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

print('-' * 30)
print('{:^30}'.format(' COLÉGIO TUTTI FRUTTI '))
print('-' * 30)

dados = list()

while True:
    nome = str(input('Digite o seu nome: '))
    nota01 = float(input('Nota 01: '))
    nota02 = float(input('Nota 02: '))
    media = (nota01 + nota02) / 2
    dados.append([nome, [nota01, nota02], media])
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

print('-' * 30)
print('{:^30}'.format(' BOLETIM '))
print('-' * 30)
print('{:<10}{:^10}{:>10}'.format('Nº','Nome','Média'))
print('-' * 30)
for i, a in enumerate(dados):
    print(f'{i:<10}{a[0]:^10}{a[2]:>10.1f}')

while True:
    print('-' * 30)
    nota_geral = int(input('Mostrar nota de qual aluno? (999 para interromper) '))
    if nota_geral == 999:
        break
    if nota_geral <= len(dados) - 1:
        print(f'Notas do aluno(a) {dados[nota_geral][0]} são {dados[nota_geral][1]}')
print('{:=^40}'.format(' FIM DO PROGRAMA '))
