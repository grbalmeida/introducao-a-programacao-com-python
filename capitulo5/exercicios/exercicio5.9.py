# Exercício 5.9: Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20
dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

if divisor == 0:
    print("Não é possível dividir por zero!")
else:
    quociente = 0
    resto = abs(dividendo)
    abs_divisor = abs(divisor)

    while resto >= abs_divisor:
        resto -= abs_divisor
        quociente += 1

    if (dividendo < 0) != (divisor < 0):
        quociente = -quociente
    
    if dividendo < 0:
        resto = -resto

    print(f"{dividendo} / {divisor} = {quociente}")
    print(f"Resto = {resto}")