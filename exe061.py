#Refaça o desafio 051, lendo o primeiro termo e a razão de uma P.A., mostrando os 10 primeiros termos da progressão usando
#a estrutura while.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
progressao = termo
contador = 1

while contador <= 10:
    print('{} -> '.format(progressao), end='')
    progressao += razao
    contador += 1
print('Fim.')