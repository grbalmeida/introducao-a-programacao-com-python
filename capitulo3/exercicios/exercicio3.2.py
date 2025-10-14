# Exercício 3.2: Complete a tabela a seguir, respondendo True ou False. Considere a = 4, b = 10, c = 5.0, d = 1 e f = 5

a = 4
b = 10
c = 5.0
d = 1
f = 5

assert (a == c) == False # pois 4 é diferente de 5.0
assert (a < b) == True # pois 4 é menor que 10
assert (d > b) == False # pois 1 não é maior 10
assert (c != f) == False # pois embora 5.0 seja flutuante e 5 seja inteiro, ambos representam o mesmo número
assert (a == b) == False # pois 4 não é igual 10
assert (c < d) == False # pois 5.0 não é menor que 1
assert (b > a) == True # pois 10 é maior que 4
assert (c >= f) == True # pois 5.0 é maior ou igual a 5
assert (f >= c) == True # pois 5 é maior ou igual a 5.0
assert (c <= c) == True # pois 5.0 é menor ou igual a 5.0
assert (c <= f) == True # pois 5.0 é menor ou igual a 5