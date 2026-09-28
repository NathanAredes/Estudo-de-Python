'''
---Operadores Aritméticos

+ Adição
- Subtração
* Multiplicação
** Exponenciação
/ Divisão
// Divisão Inteira
% Resto da Divisão
x**(1/2) Raiz Quadrada
x**(1/3) Raiz Cúbica

---Ordem de Precedência

1. Parênteses
2. Exponenciação
3. Multiplicação, Divisão, Divisão Inteira e Resto da Divisão
4. Adição e Subtração

'''

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2

print('A soma é {} A subtração é {} A multiplicação é {} A divisão é {:.2f}'. format(s, sub, m, d), end=' ')
# O {:.2f} é usado para formatar a saída da divisão, limitando a 2 casas decimais. 
# O end=' ' é usado para evitar a quebra de linha após a impressão da divisão.

print('A divisão inteira é {} A exponenciação é {} O resto da divisão é {}'. format(di, e, r))