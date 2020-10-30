#Faça um programa que leia o sexo de uma pessoa, mas só aceite 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
#até ter um valor correto.

sexo = str(input('Digite o seu sexo: ')).strip().upper()[0] #fatia a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Tente novamente: ')).strip().upper()[0]
print('Sexo {}. Registrado. Obrigada.'.format(sexo))