# Exercício 5.15: Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto:

# Código | Preço
#    1   | 0.50
#    2   | 1.00
#    3   | 4.00
#    5   | 7.00
#    9   | 8.00

# Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro "Código inválido".

total_compras = 0

while True:
    codigo = int(input("Digite o código do produto ou 0 para sair: "))

    if codigo == 0:
        break

    if codigo not in [1, 2, 3, 5, 9]:
        print("Código inválido!")
        continue 

    quantidade_comprada = int(input("Digite a quantidade comprada: "))

    if quantidade_comprada <= 0:
        print("A quantidade deve ser maior que 0")
    else: 
        if codigo == 1:
            preco_unidade = 0.50
        elif codigo == 2:
            preco_unidade = 1.00
        elif codigo == 3:
            preco_unidade = 4.00
        elif codigo == 5:
            preco_unidade = 7.00
        elif codigo == 9:
            preco_unidade = 8.00

        total_compras += (quantidade_comprada * preco_unidade)

print(f"Total das compras: R${total_compras:,.2f}")