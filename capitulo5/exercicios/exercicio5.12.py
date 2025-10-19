# Exercício 5.12: Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e você deverá considerá-lo para o cálculo de juros do mês seguinte.
deposito_inicial = float(input("Digite o depósito inicial: "))
deposito_mensal = float(input("Digite o depósito mensal: "))
taxa_juros = float(input("Digite a taxa de juros da poupança: "))
total_juros_periodo = 0
mes = 1
montante = deposito_inicial

print(f"Depósito inicial: {deposito_inicial:,.2f}")

while mes <= 24:
    juros_mes = (montante * taxa_juros / 100)
    montante += juros_mes
    total_juros_periodo += juros_mes
    print(f"Mês {mes}: R${montante:,.2f}")
    mes += 1
    montante += deposito_mensal
    
print(f"Total de juros no período: R${total_juros_periodo:,.2f}")