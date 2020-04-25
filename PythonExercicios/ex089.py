"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno indivualmente."""
final = []
boletim = []
aluno = []
notas = []
media = []
contar = individual = 0
while True:
    aluno.append(str(input('Nome do aluno: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media.append((notas[0] + notas[1]) / 2)
    boletim.append(aluno[:])
    boletim.append(notas[:])
    boletim.append(media[:])
    final.append(boletim[:])
    aluno.clear()
    notas.clear()
    media.clear()
    boletim.clear()
    contar += 1
    resp = str(input('Quer continuar ? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
for c in final:
    print(f'O aluno(a) \033[4;30m{c[0][0]}\033[m teve as notas \033[1;34m{c[1][0]}\033[m e \033[1;34m{c[1][1]}\033[m e teve uma média de \033[1;33m{c[2][0]}\033[m')
print('-=' * 30)
for c, a in enumerate(range(0, contar)):
    print(f'[ {a} ] {final[c][0][0]}')
while individual != 999:
    individual = int(input('Digite um número acima pra ver nota ou 999 pra sair: '))
    if individual != 999:
        print(f'{final[individual][0][0]} notas \033[1;34m{final[individual][1][0]}\033[m e \033[1;34m{final[individual][1][1]}\033[m')
