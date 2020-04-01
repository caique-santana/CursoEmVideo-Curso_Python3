# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
numero = int(input('Digite um número: '))
print('Você digitou {}.\nO dobro dele é {}.\nO Triplo dele é {}.\nE sua raiz quadrada é {:.2f}'.format(numero, numero*2, numero*3, numero**0.5))
print('')

# Gustavo Guanabara
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O tripo de {} vale {}. \nA raiz quadrada de {} é igual a {}.'.format(n, t, n, r))
# Outra forma
n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O tripo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2))))