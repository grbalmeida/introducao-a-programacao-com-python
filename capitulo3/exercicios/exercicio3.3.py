# Exercício 3.3: Complete a tabela a seguir utilizando
a = True
b = False
c = True

assert (a and b) == False
assert (b and b) == False
assert (not c) == False
assert (not b) == True
assert (not a) == False
assert (a and b) == False
assert (b and c) == False
assert (a or c) == True
assert (b or c) == True
assert (c or a) == True
assert (c or b) == True
assert (c or c) == True
assert (b or b) == False