# Faça um programa que solicite ao usuário que digite algo 
# Em seguida, imprima o tipo primitivo desse valor e todas as informações possíveis sobre ele usando os métodos disponíveis para strings.

valor = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(valor))
print('É um número?', valor.isnumeric())
print('É alfabético?', valor.isalpha())
print('É alfanumérico?', valor.isalnum())
print('Está em maiúsculas?', valor.isupper())
print('Está em minúsculas?', valor.islower())
print('É um espaço?', valor.isspace())
# O método .isspace() é usado para verificar se a string é composta apenas por espaços em branco e retorna True ou False.

print('Está capitalizada?', valor.istitle())
# O método .istitle() é usado para verificar se a string está capitalizada
# Ou seja, se a primeira letra de cada palavra está em maiúscula e as demais em minúscula. Ele retorna True ou False.

print('É um identificador válido?', valor.isidentifier())
# O método .isidentifier() é usado para verificar se a string é um identificador válido em Python
# Ou seja, se pode ser usada como nome de variável, função, etc. Ele retorna True ou False.

print('É um dígito?', valor.isdigit())
# O metodo .isdigit() é usado para verificar se a string é composta apenas por dígitos(numeros inteiros) e retorna True ou False.

print('É um número de ponto flutuante?', valor.replace('.', '', 1).isdigit()) # não funciona direito
# O método .replace() é usado para substituir um caractere por outro em uma string.