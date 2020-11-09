#Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
#conteúdo da estrutura na tela.

aluno = dict()

aluno['nome'] = str(input('Aluno(a): '))
aluno['media'] = float(input('Média: '))
print(f'Aluno(a) {aluno["nome"]}.')
print(f'Média é igual {aluno["media"]}')
if aluno['media'] >= 7.0:
    aluno['situacao'] = 'Aprovado!'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Em recuperação.'
else:
    aluno['situacao'] = 'Reprovado!'
print(f'Situação: {aluno["situacao"]}')