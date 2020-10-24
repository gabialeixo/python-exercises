#Escreve um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça pro usuário tentar descobrir qual
#foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
numero = int(input('Adivinhe o número que eu estou pensando, entre 0 e 5: '))
adivinhacao = random.randint(0,5)
if numero == adivinhacao:
    print('ACERTOU! Você é um gênio! Eu pensei no número: {}'.format(adivinhacao))
else:
    print('Como eu pensei... Meu número é: {}! Tente de novo.'.format(adivinhacao))