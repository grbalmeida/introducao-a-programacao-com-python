# Exercício 4.4: Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input("Digite o seu salário: "))

if salario > 1250:
    aumento = salario * 10 / 100

if salario <= 1250:
    aumento = salario * 15 / 100

novo_salario = salario + aumento

print(f"Salário atual: {salario:5.2f}")
print(f"Valor do aumento: {aumento:5.2f}")
print(f"Novo salário: {novo_salario:5.2f}")