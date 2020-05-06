"""Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""
# Caique Santana
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
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for p, g in enumerate(gols):
    print(f'    => Na partida {p+1}, fez {g} gols.')
print(f'Foi um total de {tot} gols.')

# Gustavo Guanabara
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.' )
print(f'Foi um total de {jogador["total"]} gols.')
