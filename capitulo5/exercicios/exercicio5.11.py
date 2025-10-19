# Exercício 5.11: Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
deposito_inicial = float(input("Digite o depósito inicial: "))
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
    
print(f"Total de juros no período: R${total_juros_periodo:,.2f}")