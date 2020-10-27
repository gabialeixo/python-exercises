#Faça um programa que mostre na tela uma contagem regressiva par o estouro de fogos de artificio, indo de 10 até 0,
#com pausa de 1 segundo entre eles.

import emoji
from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks: FELIZ ANO NOVO!! :fireworks:', use_aliases=True))