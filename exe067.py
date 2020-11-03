#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa
#será interrompido quando o número solicitado for negativo.

print('=' * 7)
print('TABUADA')
print('=' * 7)

tabuada = num = contador = 0

while True:
    num = int(input('Você quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    for contador in range(1,11):
        tabuada = num * contador
        print(f'{num} x {contador} = {tabuada}')
    print('-' * 20)
print('PROGRAMA TABUADA ENCERRADO! Volte quando quiser!')