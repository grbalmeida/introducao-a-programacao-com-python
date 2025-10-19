# Exercício 5.20: O que acontece se digitarmos 0.001 no programa anterior? Caso ele não funcione, altere-o de forma a corrigir o problema.

# Resposta: Ele entra em loop infinito, podemos validar o if valor == 0, para if valor < D('0.01')

# Programa 5.1: Contagem de cédulas
from decimal import Decimal
D = Decimal
valor = D(input("Digite o valor a pagar: "))

cédulas = 0
moedas = 0
atual = D('100')
apagar = valor

if valor < D('0.01'):
    print("Informe um valor maior que 0.01")
else:
    while True:

        if atual <= apagar:
            apagar -= atual

            if atual >= 1:
                cédulas += 1
            else:
                moedas += 1
        else:
            if atual >= 1 and cédulas > 0:
                print(f"{cédulas} cédula(s) de R${atual}")
            elif atual < 1 and moedas > 0:
                print(f"{moedas} moeda(s) de R${atual}")

            if apagar == 0:
                break
            if atual == D('100'):
                atual = D('50')
            elif atual == D('50'):
                atual = D('20')
            elif atual == D('20'):
                atual = D('10')
            elif atual == D('10'):
                atual = D('5')
            elif atual == D('5'):
                atual = D('1')
            elif atual == D('1'):
                atual = D('0.50')
            elif atual == D('0.50'):
                atual = D('0.10')
            elif atual == D('0.10'):
                atual = D('0.05')
            elif atual == D('0.05'):
                atual = D('0.02')
            elif atual == D('0.02'):
                atual = D('0.01')

            cédulas = 0
            moedas = 0