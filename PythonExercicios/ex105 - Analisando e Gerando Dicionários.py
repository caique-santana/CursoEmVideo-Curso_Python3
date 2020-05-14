"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função."""
# Caique Santana


def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('-' * 30)
    turma = {'total': 0, 'maior': 0, 'menor': 0, 'média': 0}
    for c in num:
        if turma['total'] == 0:
            turma['maior'] = c
            turma['menor'] = c
        else:
            if c > turma['maior']:
                turma['maior'] = c
            if c < turma['menor']:
                turma['menor'] = c
        turma['total'] += 1
    turma['média'] = sum(num) / turma['total']
    if sit:
        if turma['média'] < 5:
            turma['situação'] = 'RUIM'
        elif turma['média'] < 7:
            turma['situação'] = 'RAZOÁVEL'
        elif turma['média'] > 7:
            turma['situação'] = 'BOA'
    return turma


# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)

# Gustavo Guanabara
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maio'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
