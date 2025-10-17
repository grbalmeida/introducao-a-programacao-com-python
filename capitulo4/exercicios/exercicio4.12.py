# Exercício 4.12: Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

# Preço por tipo e faixa de consumo
# Tipo        | Faixa         | Preço
# Residencial | Até 500       | R$ 0.40
#             | Acima de 500  | R$ 0.65
# Comercial   | Até 1000      | R$ 0.55
#             | Acima de 1000 | R$ 0.60
# Industrial  | Até 5000      | R$ 0.55
#             | Acima de 5000 | R$ 0.60

quantidade_kwh = float(input("Digite a quantidade de kWh consumida: "))
tipo_instalacao = input("Digite o tipo de instalação R(Residencial), I(Industrial), C(Comercial): ")
tipo_instalacao_valido = True

if tipo_instalacao == "R":
    if quantidade_kwh <= 500:
        preco_por_kw = 0.40
    else:
        preco_por_kw = 0.65
elif tipo_instalacao == "C":
    if quantidade_kwh <= 1000:
        preco_por_kw = 0.55
    else:
        preco_por_kw = 0.60
elif tipo_instalacao == "I":
    if quantidade_kwh <= 5000:
        preco_por_kw = 0.55
    else:
        preco_por_kw = 0.60
else:
    tipo_instalacao_valido = False
    print("Tipo de instalação inválido!")

if tipo_instalacao_valido:
    print(f"Quantidade de kWh: {quantidade_kwh:,.2f}")
    print(f"Tipo de instalação: {tipo_instalacao}")
    print(f"Preço por kWh: R${preco_por_kw:,.2f}")
    print(f"Preço a pagar: R${quantidade_kwh * preco_por_kw:,.2f}")