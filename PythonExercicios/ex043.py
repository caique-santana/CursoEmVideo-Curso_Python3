""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do Peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida """
# Meu
print('\033[1;34m-=-\033[m'*10)
print('\033[33mVamos calcular o seu IMC\033[m')
print('\033[1;34m-=-\033[m'*10)
peso = float(input('Informe o seu peso em Kg: '))
altura = float(input('Informe a sua altura em metros: '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Seu IMC é {:.2f}\nVocê está \033[1;33mabaixo do peso\033[m'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.2f}\nVocê está no seu \033[1;32mpeso ideal\033[m'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {:.2f}\nVocê está com \033[31msobrepeso\033[m'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é {:.2f}\nVocê está com \033[1;31mobesidade\033[m'.format(imc))
else:
    print('Seu IMC é {:.2f}\nVocê está com \033[1m\033[4;31mobesidade morbida\033[m'.format(imc))
