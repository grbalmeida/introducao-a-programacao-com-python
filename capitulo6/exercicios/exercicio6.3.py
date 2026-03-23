# Exercício 6.3: Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos

L1 = [1, 2, 3, 4, 5, 6]
L2 = [3, 4, 5, 8, 9, 10]
L3 = []
x = 0

while x < len(L1):
    if L1[x] not in L3:
        L3.append(L1[x])
    x += 1

x = 0

while x < len(L2):
    if L2[x] not in L3:
        L3.append(L2[x])
    x += 1

print(L3)