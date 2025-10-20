# Programa 5.2: Tabuada com repetições aninhadas
tabuada = 1

while tabuada <= 10:
    número = 1
    
    while número <= 10:
        print(f"{tabuada} x {número} = {tabuada * número}")
        número += 1
    
    tabuada += 1