# Exercício 3.6: Escreva uma empressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores ou iguais a 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3

matéria1 = 7
matéria2 = 7
matéria3 = 7
aprovado = matéria1 >= 7 and matéria2 >= 7 and matéria3 >= 7
assert aprovado == True

matéria1 = 6.9
matéria2 = 7
matéria3 = 8
aprovado = matéria1 >= 7 and matéria2 >= 7 and matéria3 >= 7
assert aprovado == False