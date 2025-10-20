# Exercício 5.27: Escreva um programa que verifique se um número é palíndromo. Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos. Exemplo: 454, 10501

# Solução com str()
"""
10501
0 = 4
1 = 3
2 = 2
3 = 1
4 = 0
"""
numero = int(input("Digite um número: "))
numero_str = str(numero)
contador_inverso = len(numero_str) - 1
contador = 0
eh_palindromo = True

while contador_inverso >= 0:
    if not numero_str[contador_inverso] == numero_str[contador]:
        eh_palindromo = False
        break

    contador_inverso -= 1
    contador += 1

if eh_palindromo:
    print(f"{numero} é palíndromo")
else:
    print(f"{numero} não é palíndromo")