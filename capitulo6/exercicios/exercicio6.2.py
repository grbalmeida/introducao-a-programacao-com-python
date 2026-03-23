# Exercício 6.2 Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

L1 = []
L2 = []

while True:
    n = int(input("Digite um número para ser adicionado à primeira lista: (0 para sair) "))
    if n == 0:
        break
    L1.append(n)

while True:
    n = int(input("Digite um número para ser adicionado à segunda lista: (0 para sair) "))
    if n == 0:
        break
    L2.append(n)

L3 = L1 + L2
print("Terceira lista: ")
print(L3)