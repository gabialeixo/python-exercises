#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número inteiro: '))
dobro = n**2
triplo = n**3
raiz = n**(1/2)
print('Dobro: {}, Triplo: {}, Raiz Quadrada: {:.2f}!'.format(dobro, triplo, raiz))