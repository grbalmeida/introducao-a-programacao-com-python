# Exercício 3.8: Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

metros = float(input("Digite o valor em metros: "))
milimetros = metros * 1000
print(f"{metros} metros é igual {milimetros:5.2f} milímetros")