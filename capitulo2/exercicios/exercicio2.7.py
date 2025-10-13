# Exercício 2.7: Usando as propriedades da divisão e da multiplicação, tente entender como estes resultados são iguais:

print(0.2*6 + 8*0.3 + 7*0.5) # 7.1
print((20*6 + 8*30 + 7*50) / 100) # 7.1

# As duas expressões são iguais porque multiplicar por um número decimal (ex: 0.2) é o mesmo que multiplicar pelo inteiro correspondente e depois dividir por 10, 100, 1000..., conforme a quantidade de casas decimais.