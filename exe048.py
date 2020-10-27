#Faça um programa que calcule a soma entre todos os número ímpares que são múltiplos de três e que se encontram no 
#intervalo de 1 até 500.

s = 0
q = 0
for c in range(0, 500, 2):
    if c % 3 == 0:
        s += c
        q += 1
print('A soma de todos os números ímpares e que são múltiplos de três é {}.'.format(s))
print('A quantidade de números somados foi {}.'.format(q))
print('FIM.')