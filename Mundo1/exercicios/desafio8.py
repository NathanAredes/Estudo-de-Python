# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = float(input('Digite um valor em metros: '))

print(f'Valor em kilômetros: {valor / 1000}')
print(f'Valor em hectômetros: {valor / 100}')
print(f'Valor em decâmetros: {valor / 10}')
print(f'Valor em decímetros: {valor * 10}')
print(f'Valor em centímetros: {valor * 100}')
print(f'Valor em milímetros: {valor * 1000}')