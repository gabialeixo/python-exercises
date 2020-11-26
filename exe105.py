'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as
seguintes informações:

A) Quantidade de notas;
B) A maior nota;
C) A menor nota;
D) A média da turma;
E) A situação (opcional)

Adicione também as docstrings da função.'''

def notas(* num, sit=False):
    """
        -> Função para analisar notas e situações de diversos alunos.
        :param num: uma ou mais notas de alunos (aceita várias).
        :param sit: valor opcional, informa a situação do aluno conforme a média.
        :return: retorna um dicionário com todas as informações solicitadas.
    """
    info = dict()
    info['total'] = len(num)
    info['maior'] = max(num)
    info['menor'] = min(num)
    info['média'] = sum(num)/len(num)
    if sit:
        if info['média'] >= 7:
            info['situação'] = 'BOA'
        elif info['média'] >=5:
            info['situação'] = 'RAZOÁVEL'
        else:
            info['situação'] = 'RUIM'

    return info


#Programa principal
resp = notas(4, 3, 5, 3, sit=True)
print(resp)
#help(notas)