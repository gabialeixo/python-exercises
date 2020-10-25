#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
#1- para binário 2- para octal 3- para hexadecimal

escolha = str(input("""Este é um programa de conversão de bases! Escolha abaixo para qual deseja converter:
1 - BINÁRIO
2 - OCTAL
3 - HEXADECIMAL
"""))
if escolha == '1':
    num = int(input('Digite um número inteiro qualquer: '))
    binario = str(bin(num))
    print('O resultado da conversão ficou {}.'.format(binario))
elif escolha == '2':
    num = int(input('Digite um número inteiro qualquer: '))
    octal = str(oct(num))
    print('O resultado da conversão ficou {}.'.format(octal))
elif escolha == '3':
    num = int(input('Digite um número inteiro qualquer: '))
    hexadecimal = str(hex(num))
    print('O resultado da conversão ficou {}.'.format(hexadecimal))
print('Obrigada, nos vemos na próxima!')