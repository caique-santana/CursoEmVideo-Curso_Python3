# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input('Digite um valor em metros: '))
print('O valor digitado foi: {}m.\nEm Quilômetros: {:.3f}km.\nEm hectometros {:.2f}hm.\nEm decametros: {:.1f}dam.\nEm decimetros: {:.0f}dm.\nEm centímetros: {:.0f}cm.\nEm milímetros: {:.0f}mm.'.format(metros, (metros/1000), (metros/100), (metros/10), (metros*10), metros*100, metros*1000))

# Gustavo Guanabara
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 100
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))