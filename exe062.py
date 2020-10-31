#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
#disser que quer 0 termos.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
progressao = termo
contador = 1
total = 0
continuacao = 10

while continuacao != 0:
    total += continuacao
    while contador <= total:
        print('{} -> '.format(progressao), end='')
        progressao += razao
        contador += 1
    print('PAUSA.')
    continuacao = int(input('Você gostaria de ver mais quantos termos dessa P.A.? '))
print('Fim.')