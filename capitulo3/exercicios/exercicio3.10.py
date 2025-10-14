# Exercício 3.10: Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o salário: "))
aumento = float(input("Digite a porcentagem: "))
valor_aumento = salario * aumento / 100
novo_salario = salario + valor_aumento

print(f"Salário atual: {salario:5.2f}")
print(f"Aumento: {aumento:5.2f}%")
print(f"Valor aumento: {valor_aumento:5.2f}")
print(f"Novo salário: {novo_salario:5.2f}")
