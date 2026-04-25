# Autor: Wisley E.

num = [0] * 5
x=0
while x <5:
    num[x] = int(input(f"{x+1}° Numero: "))
    x += 1

while True :
    escolhido = int(input("Que posição vc quer imprimir? \n (0 para sair): "))
    if escolhido == 0:
        break
    elif escolhido >=6:
        print("Essa posição não existe! ")
        
    print(f"Você escolheu o numero: {num[escolhido - 1]}")
