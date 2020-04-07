"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres tem menos de 20 anos."""
# Meu
somaidade = 0
maisvelho = 0
homemvelho = ''
mulheres = 0
for c in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = int(input('''Escolha seu sexo:
    [1] Masculino
    [2] Feminino
    Escolha a opção: '''))
    somaidade += idade
    if sexo == 1 and idade > maisvelho:
        maisvelho = idade
        homemvelho = nome
    if sexo == 2 and idade < 20:
        mulheres += 1
print('A média de idade é {} anos.\nO homem mais velho é o {} com {} anos.\nMulheres com menos de 20 anos: {}'.format(somaidade / 4, homemvelho, maisvelho, mulheres))

# Gustavo Guanabara
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
