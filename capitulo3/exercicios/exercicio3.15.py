# Exercício 3.15: Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
TEMPO_PERDIDO_CADA_CIGARRO_EM_MINUTOS = 10
MINUTOS_EM_UM_DIA = 24 * 60
quantidade_cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
quantidade_anos_fumante = int(input("Digite há quantos anos você fuma: "))
dias_perdidos = (quantidade_cigarros_por_dia * TEMPO_PERDIDO_CADA_CIGARRO_EM_MINUTOS * 365 * quantidade_anos_fumante) / MINUTOS_EM_UM_DIA

print(f"Você já perdeu {int(dias_perdidos)} dia(s) por fumar!")