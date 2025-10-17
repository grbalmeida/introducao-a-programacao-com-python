# Exercício 4.10: Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você pode calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado a operação solicitada
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação: ")

operacao_valida = True

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero não é permita")
        operacao_valida = False
else:
    print("Operação inválida")
    operacao_valida = False

if operacao_valida:
    print(f"{num1} {operacao} {num2} = {resultado}")