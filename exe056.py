#Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final o programa deve mostrar a media de idade do grupo
#Qual é o nome do homem mais velho, quantas mulheres tem menos de 20 anos.

soma = 0
idade = 0
contador_idade = 0
contador_maior = 0

for c in range (1, 5):
    print('{}ª pessoa.'.format(c))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = int(input('Qual o seu sexo: \n[1] Feminino \n[2] Masculino \n'))

    soma += idade
    media_idade = soma / 4

    if sexo == 2:
        if idade > contador_maior:
            contador_maior = idade
            nome_masculino = nome
    else:
        nome_masculino = 'Não tem homem na lista!'

    if sexo == 1 and idade < 20:
        contador_idade += 1



print('A média de idade do grupo é de {}.'.format(media_idade))
print('O nome do homem mais velho é {}.'.format(nome_masculino))
print('A quantidade de mulheres menores de 20 anos é {}.'.format(contador_idade))


