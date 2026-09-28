# Escreva um programa que pergunte a quantidade de Kms percorridos por um carro alugado
# A quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo queo carro custa R$60 por dia e R$0,15 por Km rodado

dia = int(input('\nQuantos dias o carro foi alugado? '))
km = float(input('Quantos Kms foi rodado com o carro? '))

preco = (60 * dia) + (km * 0.15)

print(f'Valor a pagar: R${preco:.2f}\n')