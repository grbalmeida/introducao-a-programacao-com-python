# Exercício 5.7: Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.

n = int(input("Tabuada de: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

x = inicio

while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x += 1