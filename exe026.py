#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "a" apareceu {} vezes!'.format(frase.count('A')))
print('A letra "a" apareceu pela primeira vez na {}ª posição da frase!'.format(frase.find('A')+1)) #pra não contar a posição 0
print('A letra "a" apareceu pela última vez na {}ª posição da frase!'.format(frase.rfind('A')+1))