""" Crie um programa que tenha um tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""
# Caique Santana
palavras = ('aprender', 'programas', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
vogais = ''
for c in palavras:
    vogais = ''
    if c.count('a') != 0:
        vogais += 'a ' * c.count('a')
    if c.count('e') != 0:
        vogais += 'e ' * c.count('e')
    if c.count('i') != 0:
        vogais += 'i ' * c.count('i')
    if c.count('o') != 0:
        vogais += 'o ' * c.count('o')
    if c.count('u') != 0:
        vogais += 'u ' * c.count('u')
    print(f'A palavra {c.upper()} tem as vogais: {vogais}')

# Gustavo Guanabara
palavras = ('aprender', 'programas', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
