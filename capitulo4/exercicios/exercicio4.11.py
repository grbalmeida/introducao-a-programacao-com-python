# Exercício 4.11: Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário: "))
quantidade_anos = int(input("Digite a quantidade de anos: "))
quantidade_meses = quantidade_anos * 12
valor_prestacao = valor_casa / quantidade_meses
valor_maximo_prestacao = salario * 0.3

print(f"Valor da casa: {valor_casa:,.2f}")
print(f"Salário: {salario:,.2f}")
print(f"Quantidade de meses: {quantidade_meses}")
print(f"Valor da prestação: {valor_prestacao:,.2f}")
print(f"Valor máximo da prestação: {valor_maximo_prestacao:,.2f}")

if valor_prestacao > valor_maximo_prestacao:
    print("O valor da prestação não pode ser maior que 30% do salário. Seu empréstimo não foi aprovado!")
else:
    print("Seu empréstimo foi aprovado!")