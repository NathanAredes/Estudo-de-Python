# sintaxe da estrutura de condição
# if condição:
#     bloco de código
# else:
#     bloco de código
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')

# Forma para casos mais simples, onde o if e else tem apenas uma linha de código
# print((conteudo1) if condição else (conteudo2))
print('carro novo' if tempo <= 3 else 'carro velho')