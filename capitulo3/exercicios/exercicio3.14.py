# Exercício 3.14: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos os quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado

CUSTO_DIARIO = 60
CUSTO_POR_KM = 0.15

km_percorridos = float(input("Digite a quantidade de km percorridos: "))
quantidade_dias = int(input("Digite a quantidade de dias: "))
preco_a_pagar = (quantidade_dias * CUSTO_DIARIO) + (km_percorridos * CUSTO_POR_KM)

print(f"Preço a pagar: {preco_a_pagar:5.2f}")