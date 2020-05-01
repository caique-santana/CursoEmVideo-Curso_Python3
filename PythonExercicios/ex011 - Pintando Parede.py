# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
altura = float(input('Qual a altura da parede ? '))
largura = float(input('Qual a largura da parede ? '))
area = largura * altura
print('Largura: {}m.\nAltura: {}m.\nÁrea: {:.2f}m².\nA quantidade de tinta necessária vai ser: {:.2f}L.'.format(largura, altura, area, area/2))

# Gustavo Guanabara
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua áera é de {}m².'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))