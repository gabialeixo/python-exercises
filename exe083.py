#Crie um programa que o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão
#passada está com parênteses abertos e fechados na ordem correta.

pilha = list()

expressao = str(input('Digite uma expressão: '))

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão está incorreta.')

