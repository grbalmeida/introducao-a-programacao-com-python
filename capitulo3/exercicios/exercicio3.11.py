# Exercício 3.11: Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar
preco_mercadoria = float(input("Digite o valor da mercadoria: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
valor_desconto = preco_mercadoria * percentual_desconto / 100
preco_a_pagar = preco_mercadoria - valor_desconto

print(f"Preço original da mercadoria: {preco_mercadoria:5.2f}")
print(f"Percentual de desconto: {percentual_desconto:5.2f}")
print(f"Valor do desconto: {valor_desconto:5.2f}")
print(f"Preço a pagar: {preco_a_pagar:5.2f}")