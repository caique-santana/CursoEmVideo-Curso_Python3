"""Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador."""
# Caique Santana
jogadores = list()
dados = dict()
gols = list()
total = 0
while True:
    dados['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou ? '))
    for c in range(0, partidas):
        num = int(input(f'Quantos gols na partida {c+1} ? '))
        gols.append(num)
        total += num
    dados['gols'] = gols[:]
    dados['total'] = total
    gols.clear()
    total = 0
    jogadores.append(dados.copy())
    resp = str(input('Quer continuar ? [S/N] '))
    while resp not in 'SsNn':
        print('ERRO! Digite apenas S ou N.')
        resp = str(input('Quer continuar ? [S/N] '))
    if resp in 'Nn':
        break
    print('-' * 50)
print('-=' * 30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 42)
for k, v in enumerate(jogadores):
    print(f'{k:<2}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    print('-' * 42)
    opcao = int(input('Mostra dados de qual jogador [999 PARA] ? '))
    if opcao == 999:
        break
    elif opcao > len(jogadores) - 1:
        print(f'ERRO! Não existe jogador com código {opcao}! Tente novamente.')
    else:
        print('-' * 2, 'LEVANTAMENTO DO JOGADOR', f'{jogadores[opcao]["nome"]}')
        for k, v in enumerate(jogadores[opcao]["gols"]):
            print(f'    No jogo {k+1} fez {v} gols.')
print('<< VOLTE SEMPRE >>')

# Gustavo Guanabara
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
