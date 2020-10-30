#Melhore o jogo do desafio028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
#adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

contador = 0
numero = int(input('Adivinhe o número que eu estou pensando, entre 0 e 10: '))
adivinhacao = random.randint(0,10)
while numero != adivinhacao:
    numero = int(input('Você errou. Tente novamente: '))
    contador += 1
if numero == adivinhacao:
    print('Você acertou!! Levou {} tentativas para adivinhar!'.format(contador))
print('Acabou!')