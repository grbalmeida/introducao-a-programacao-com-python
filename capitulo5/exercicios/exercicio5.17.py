# Exercício 5.17: O que acontece se digitarmos 0 (zero) no valor a pagar?

# Resposta: Ele mostra a linha "0 cédula(s) de R$50"
# Uma solução seria colocar um validação para o total ser maior que 0

# Programa 5.1: Contagem de cédulas
valor = int(input("Digite o valor a pagar: "))

cédulas = 0
atual = 50
apagar = valor

if valor == 0:
    print("Informe um valor maior que 0")
else:
    while True:
        if atual <= apagar:
            apagar -= atual
            cédulas += 1
        else:
            print(f"{cédulas} cédula(s) de R${atual}")

            if apagar == 0:
                break
            if atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            cédulas = 0