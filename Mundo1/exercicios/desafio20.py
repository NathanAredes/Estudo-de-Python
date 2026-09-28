# Omesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle
aluno1 = input('\nPrimeiro aluno: ') 
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ') 
ordem = [aluno4, aluno3, aluno2, aluno1]
shuffle(ordem)
print(f'A ordem de apresentação sera:')
print(ordem)