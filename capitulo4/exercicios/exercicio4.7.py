# Exercício 4.7: Analise o Programa 4.3. Faz sentido usar o else nesse programa? Explique sua resposta.

# Programa 4.3: Cálculo do Imposto de Renda
salário = float(input("Digite o salário para cálculo do imposto: "))
base = salário
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000

if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)

print(f"Salário: R${salário:6.2f} Imposto a pagar: R${imposto:6.2f}")

# Resposta: Não, porque senão os valores de imposto seriam negativo se o salário fosse menor que 1000 reais
# Sem contar que dada a progressividade do imposto, ambas as condições podem ser verdadeiras ao mesmo tempo, levando em conta o valor R$ 5000,00, o imposto cobrado sem else seria R$ 1100.00 reais e com else R$ 700.00