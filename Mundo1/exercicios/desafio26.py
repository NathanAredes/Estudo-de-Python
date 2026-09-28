# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('\nDigite alguma frase: ').strip().upper()
print(f'Quantidade de A encontrados: {frase.count('A')}')
print(f'Posição do primeiro A: {frase.find('A')+1}')
print(f'Posição do ultimo A: {frase.rfind('A')+1}')