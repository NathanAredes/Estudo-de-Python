# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# E mostre quantos dólares ela pode comprar. Considere $1,00 = R$4,95

reais = float(input('Digite o quanto dinhiro você tem: R$'))

print(f'Você pode pegar até US${reais / 4.95:.2f}')