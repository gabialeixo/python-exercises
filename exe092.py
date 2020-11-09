#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se por
#acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
#além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

ano = date.today().year
dados = dict()
dados['nome'] = str(input('Digite o seu nome: '))
nascimento = int(input('Digite o seu ano de nascimento: '))
dados['idade'] = ano - nascimento
dados['ctps'] = int(input('Número da CTPS (Digite 0 se não tiver): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    aposentadoria = dados['contratacao'] - nascimento
    idade_aposentadoria = aposentadoria + 35
    dados['salario'] = float(input('Salário: R$'))
if dados['ctps'] == 0:
    print(f'Nome: {dados["nome"]}.')
    print(f'Idade: {dados["idade"]}.')
    print('Não possui CTPS.')

print('{:=^40}'.format(' DADOS CADASTRADOS '))
print(f'Nome: {dados["nome"]}.')
print(f'Idade: {dados["idade"]}.')
print(f'CTPS nº: {dados["ctps"]}.')
print(f'Ano da primeira contratação: {dados["contratacao"]}')
print(f'Primeiro salário: R${dados["salario"]:.2f}.')
print(f'Idade permitida para aposentadoria: {idade_aposentadoria}')
print('{:=^40}'.format(' FIM DO PROGRAMA '))