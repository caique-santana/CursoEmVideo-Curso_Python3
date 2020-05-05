"""Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""
dados = {}
gols = []
tot = 0
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou ? '))
for c in range(0, partidas):
    num = (int(input(f'Quantos gols na partida {c+1} ? ')))
    gols.append(num)
    tot += num
dados['gols'] = gols
dados['total'] = tot
print('-=' * 30)
print(dados)
print('-=' * 30)
for i, k in dados.items():
    print(f'O campo {i} tem o valor {k}.')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {partidas}.')
for p, g in enumerate(gols):
    print(f'    => Na partida {p+1}, fez {g} gols.')
print(f'Foi um total de {tot} gols.')
