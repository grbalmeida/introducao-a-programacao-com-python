# Exercício 4.6: Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km, e R$ 0,45 para viagens mais longas
distancia = float(input("Informe a distância que deseja percorrer em km: "))

if distancia <= 200:
    preco_passagem = distancia * 0.5
else:
    preco_passagem = distancia * 0.45

print(f"Para a distância de {distancia:5.2f} km você irá pagar {preco_passagem:5.2f}")