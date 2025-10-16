# Programa 4.10: Planos da Tchau com elif
válido = True
plano = input("Qual é o seu plano de celular? ")

if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.20
    preço = 50
elif plano == "falomuito":
    minutos_no_plano = 500
    extra = 0.15
    preço = 99
else:
    válido = False

if not válido:
    print(f"Erro: Não conheço este plano {plano}")
else:
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar:")
    print(f"Preço do plano R${preço:10.2f}")
    suplemento = 0

    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    
    print(f"Suplemento     R${suplemento:10.2f}")
    print(f"Total          R${preço + suplemento:10.2f}")