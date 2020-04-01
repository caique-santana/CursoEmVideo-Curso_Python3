# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
print('As duas notas do aluno foi {} e {}.\nA média desse aluno é {:.1f}'.format(nota1, nota2, media))
if media >= 5:
    print('APROVADO')
else:
    print('REPROVADO')

# Gustavo Guanabara

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2)/2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, média))
