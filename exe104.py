#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que
#fazendo a validação para aceitar apenas um valor numérico. EX = n=leiaInt('Digite um n).

def leiaInt(txt):
    t = False
    valor = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            t = True
        else:
            print('ERRO! Digite um número inteiro válido.')
        if t:
            break
    return valor


#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')