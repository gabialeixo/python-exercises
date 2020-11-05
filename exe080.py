#Crie um programa que o usuário possa digitar cinco valores e cadastre-os em uma lista, já na posição correta da inserção
#sem usar sort(). No final mostre a lista ordenada na tela.

valores = list()

for c in range(0,5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(valores):
            if num <= valores[posicao]:
                valores.insert(posicao, num)
                print(f'Adicionado na posição {posicao} da lista.')
                break
            posicao += 1

print('-' * 50)
print(f'Os valores digitados em ordem, foram: {valores}')

        