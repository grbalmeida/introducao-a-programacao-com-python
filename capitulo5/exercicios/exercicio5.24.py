# Exercício 5.24: Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos
n = int(input("Digite a quantidade de números primos que deseja: "))

if n < 1:
    print("Informe um número maior ou igual a 1")
else:
    numero = 2
    quantidade_primos = 0

    while quantidade_primos < n:
        contador = 1
        quantidade_divisores = 0

        while contador <= numero:
            if numero % contador == 0:
                quantidade_divisores += 1

            contador += 1

        if quantidade_divisores <= 2:
            quantidade_primos += 1
            print(numero)
        
        numero += 1