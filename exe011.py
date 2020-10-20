#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la.
#Sabendo que cada litro de tinta pinta uma área de 2m².

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
tinta = area / 2
print('A área total da sala é {:.2f}m² e será necessário {:.1f} litros de tinta para pintá-la.'.format(area, tinta))