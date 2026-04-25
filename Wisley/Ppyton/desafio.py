# num = float(input("Digite o numero: "))

# def impapar(a):
#     if a % 2 == 0:
#          print("Par")
#     else:
#          print("Impar")    

# impapar(num)        

num1 = int(input('1° numero: '))
num2 = int(input('2° numero: '))

def maximo(valor1, valor2):
    if valor1 > valor2:
        print(f"O Maior numero é: {valor1}")
    else:
        print(f"O Maior numero é: {valor2}")

maximo(num1, num2)