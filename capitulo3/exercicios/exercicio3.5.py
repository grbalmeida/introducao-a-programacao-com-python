# Exercício 3.5: Calcule o resultado da expressão A > B and C or D, utilizando os valores da tabela a seguir
# A  | B | C     | D     | Resultado
# 1  | 2 | True  | False |
# 10 | 3 | False | False |
# 5  | 1 | True  | True  |

A = 1
B = 2
C = True
D = False
assert (A > B and C or D) == False

A = 10
B = 3
C = False
D = False
assert (A > B and C or D) == False

A = 5
B = 1
C = True
D = True
assert (A > B and C or D) == True