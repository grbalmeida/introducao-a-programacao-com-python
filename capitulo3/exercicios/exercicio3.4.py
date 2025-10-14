# Exercício 3.4: Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00

salario = 1200
paga_imposto = salario > 1200
assert paga_imposto == False
salario = 1201
paga_imposto = salario > 1200
assert paga_imposto == True