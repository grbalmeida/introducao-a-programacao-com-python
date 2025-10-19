# Exercício 5.14: Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução exiba a quantidade de números digitados, assim como a soma e a média aritmética

quantidade_numeros = 0
soma = 0

while True:
    numero = int(input("Digite um número ou 0 para sair: "))

    if numero == 0:
        break

    quantidade_numeros += 1
    soma += numero

if quantidade_numeros > 0:
    media = soma / quantidade_numeros
    print(f"Quantidade de números digitados: {quantidade_numeros}")
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
else:
    print("Nenhum número foi digitado.")