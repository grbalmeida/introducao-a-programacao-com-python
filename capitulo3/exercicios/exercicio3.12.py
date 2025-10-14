# Exercício 3.12: Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem
distancia_a_percorrer = int(input("Digite a distância a percorrer em quilômetros: "))
velocidade_media = int(input("Digite a velocidade média em quilômetros por hora: "))
tempo_viagem_horas = int(distancia_a_percorrer // velocidade_media)
tempo_viagem_minutos = int(((distancia_a_percorrer / velocidade_media) - tempo_viagem_horas) * 60)
print(f"Para percorrer {distancia_a_percorrer} quilômetros a {velocidade_media} quilômetros/hora você levará {tempo_viagem_horas} hora(s) e {tempo_viagem_minutos} minuto(s)")