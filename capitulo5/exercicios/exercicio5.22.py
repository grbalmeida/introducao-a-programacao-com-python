# Exercício 5.22: Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão e sair. Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.

while True:
    print("Escolha a operação da tabuada")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("5 - Sair")
    
    opcao = int(input("Digite a opção: "))

    if opcao not in [1, 2, 3, 4, 5]:
        print("Operação inválida!")
        continue

    if opcao == 5:
        print("Programa encerrado!")
        break

    tabuada = 1

    while tabuada <= 10:
        número = 1
        
        while número <= 10:
            if opcao == 1:
                resultado = tabuada + número
                operador = '+'
            elif opcao == 2:
                resultado = tabuada - número
                operador = '-'
            elif opcao == 3:
                resultado = tabuada / número
                operador = '/'
            elif opcao == 4:
                resultado = tabuada * número
                operador = 'x'

            print(f"{tabuada} {operador} {número} = {resultado}")
            número += 1
        tabuada += 1
