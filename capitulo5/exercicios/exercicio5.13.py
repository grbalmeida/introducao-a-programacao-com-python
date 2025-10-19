# Exercício 5.13: Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
valor_inicial_divida = float(input("Digite o valor inicial da dívida: "))
juro_mensal = float(input("Digite o juro mensal: "))
abatimento_mensal = float(input("Digite o valor que será pago mensalmente: "))

numero_meses_divida_ser_paga = 0
total_pago = 0
total_juros_pago = 0
total_juros_pago_mes = 0

valor_divida = valor_inicial_divida

print(f"Valor inicial da dívida: R${valor_inicial_divida:,.2f}")
print(f"Juro mensal: {juro_mensal:,.2f}")
print(f"Abatimento mensal: R${abatimento_mensal:,.2f}")

while valor_divida > 0:
    pagamento_mes = abatimento_mensal

    if abatimento_mensal > valor_divida:
        pagamento_mes = valor_divida

    total_pago += pagamento_mes

    total_juros_pago_mes = valor_divida * juro_mensal / 100
    total_juros_pago += total_juros_pago_mes
    valor_divida += total_juros_pago_mes
    valor_divida -= pagamento_mes
    numero_meses_divida_ser_paga += 1

print(f"Número de meses para a dívida ser paga: {numero_meses_divida_ser_paga}")
print(f"Total pago: R${total_pago:,.2f}")
print(f"Total juros pagos: R${total_juros_pago:,.2f}")