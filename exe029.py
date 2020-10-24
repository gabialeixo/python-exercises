#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.

vel = float(input('Velocidade atual: '))
limite = vel - 80
multa = limite * 7
if vel > 80:
    print('Você foi multado!')
    print('Você ultrapassou {}km. A sua multa irá custar R${:.2f}.'.format(limite, multa))
else:
    print('Continue dirigindo com segurança!')