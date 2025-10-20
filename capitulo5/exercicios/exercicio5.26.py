# Exercício 5.26: Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado.
dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

if divisor == 0:
    print("Não é possível dividir por zero!")
else:
    resto = abs(dividendo)
    abs_divisor = abs(divisor)

    while resto >= abs_divisor:
        resto = resto - abs_divisor
    
    if dividendo < 0:
        resto = -resto

print(f"Resto de {dividendo} / {divisor} = {resto}")