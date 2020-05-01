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
    print('Seu IMC é {:.1f}\nVocê está \033[1;33mABAIXO DO PESO\033[m'.format(imc))
elif 18.5 <= imc <= 25:
    print('Seu IMC é {:.1f}\nVocê está no seu \033[1;32mPESO IDEAL\033[m'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.1f}\nVocê está com \033[31mSOBREPESO\033[m'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.1f}\nVocê está com \033[1;31mOBESIDADE\033[m'.format(imc))
else:
    print('Seu IMC é {:.2f}\nVocê está com \033[1m\033[4;31mOBESIDADE MÓRBIDA\033[m'.format(imc))

# Gustavo Guanabara
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual pe a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('Parabéns, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')

