#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

import emoji

print('=' * 14)
print(emoji.emojize(':1234: TABUADA :1234:', use_aliases=True))
print('=' * 14)

num = int(input('Digite o número que deseja a tabuada: '))
for c in range(0,11):
    tabuada = num * c
    print('{} x {} = {}'.format(num, c, tabuada))
print('Fim!')