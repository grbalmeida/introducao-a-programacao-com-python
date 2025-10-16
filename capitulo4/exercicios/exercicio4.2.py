# Exercício 4.2: Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
VELOCIDADE_MAXIMA = 80
velocidade = float(input("Digite a velocidade do seu carro em km/h: "))

if velocidade > VELOCIDADE_MAXIMA:
    valor_multa = (velocidade - VELOCIDADE_MAXIMA) * 5
    print("Você foi multado!")
    print(f"O valor da multa é R${valor_multa:5.2f}")
    