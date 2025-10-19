# Exercício 5.8: Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 == 0 or num2 == 0:
    print(f"{num1} x {num2} = 0")
else:
    x = 1
    resultado = 0

    abs_num2 = abs(num2)

    while x <= abs_num2:
        resultado += num1
        x += 1

    if num2 < 0:
        resultado = -resultado

    print(f"{num1} x {num2} = {resultado}")