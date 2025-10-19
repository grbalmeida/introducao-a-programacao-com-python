# Exercício 5.10: Modifique o programa anterior para que aceite respostas com letras maiúsculas e minúsculas em todas as questões.

pontos = 0
questão = 1

# while questão <= 3:
#     resposta = input(f"Resposta da questão {questão}: ")

#     if questão == 1 and resposta == "b":
#         pontos = pontos + 1
    
#     if questão == 2 and resposta == "a":
#         pontos = pontos + 1

#     if questão == 3 and resposta == "d":
#         pontos = pontos + 1
    
#     questão = questão + 1

# print(f"O aluno fez {pontos} ponto(s)")

while questão <= 3:
    resposta = input(f"Resposta da questão {questão}: ")

    if questão == 1 and (resposta == "b" or resposta == "B"):
        pontos += 1
    elif questão == 2 and (resposta == "a" or resposta == "A"):
        pontos += 1
    elif questão == 3 and (resposta == "d" or resposta == "D"):
        pontos += 1
    
    questão += 1

print(f"O aluno fez {pontos} ponto(s)")