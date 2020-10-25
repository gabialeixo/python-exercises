#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela:
#Abaixo de 18.4: abaixo do peso / entre 18.5 e 25: peso ideal / entre 25.1 até 30: sobrepeso
#entre 30.1 até 40: obesidade / acima de 40.1: obesidade mórbida.

print('=' * 15)
print('CALCULADORA IMC')
print('=' * 15)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc <= 18.4:
    print('Seu IMC é {:.2f}. Você está abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc <=25:
    print('Seu IMC é {:.2f}. Você está no peso ideal!'.format(imc))
elif imc >=25.1 and imc <=30:
    print('Seu IMC é {:.2f}. Você está no sobrepeso!'.format(imc))
elif imc >=30.1 and imc <=40:
    print('Seu IMC é {:.2f}. Você está com obesidade!'.format(imc))
elif imc >=40.1:
    print('Seu IMC é {:.2f}. Você está com obesidade mórbida!'.format(imc))