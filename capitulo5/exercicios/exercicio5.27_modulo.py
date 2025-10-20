# Exercício 5.27: Escreva um programa que verifique se um número é palíndromo. Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos. Exemplo: 454, 10501

"""
Para o número 101
primeira entrada no loop
101 > 0:
    digito = resto da divisao de 101 por 10 igual a (1)
    inverso = 0 * 10 + (1) = 1
    numero = divisao inteira de 101 por 10 = 10

segunda entrada no loop
10 > 0:
    digito = resto da divisao de 10 por 10 igual a (0)
    inverso = 1 * 10 + 0 = 10
    numero = divisao inteira de 10 por 10 = 1

terceira entrada no loop
1 > 0:
    digito = 1 % 10 = 1
    inverso = 10 * 10 + 1 = 101
    numero = 1 // 10 = 0

ultima iteracao 0 > 0, sai do loop

no final compara inverso (101) == original (101) == True
"""

# Solução com módulo
numero = int(input("Digite um número: "))
original = numero
inverso = 0

while numero > 0:
    digito = numero % 10
    inverso = inverso * 10 + digito
    numero = numero // 10

if inverso == original:
    print(f"{original} é palíndromo")
else:
    print(f"{original} não é palíndromo")