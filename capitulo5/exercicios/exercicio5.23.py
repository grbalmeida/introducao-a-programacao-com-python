# Exercício 5.23: Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
numero = int(input("Digite um número: "))

if numero == 0 or numero == 1:
    print(f"O número {numero} não é primo")
elif numero == 2:
    print("O número 2 é primo")
elif numero % 2 == 0:
    print(f"O número {numero} não é primo")
else:
    raiz_numero = int(numero ** 0.5)
    numero_ocorrencias = 0
    divisor = 1

    while divisor <= raiz_numero:
        if numero % divisor == 0:
            numero_ocorrencias += 1

        if numero_ocorrencias > 1:
            break

        divisor += 1

    if numero_ocorrencias > 1:
        print(f"O número {numero} não é primo")
    else:
        print(f"O número {numero} é primo")