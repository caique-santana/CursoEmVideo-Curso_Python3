""" Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos."""
continuar = 'S'
maior18 = homens = mulheres = 0
while continuar == 'S':
    print('-*' * 20)
    print('CADASTRE UMA PESSOA')
    print('-*' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper()
    print('-' * 20)
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
