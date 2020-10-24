#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule preço da passagem, cobrando
#R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longas.

distancia = float(input('Quantos km até o seu destino? '))
if distancia <=200:
    curta = distancia * 0.50
    print('A sua viagem é curta. O preço da passagem é de R${:.2f}.'.format(curta))
else:
    longa = distancia * 0.45
    print('A sua viagem é longa! O preço da passagem é de R${:.2f}.'.format(longa))