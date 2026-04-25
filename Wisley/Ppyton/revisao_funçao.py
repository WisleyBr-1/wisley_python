#Autor: Wisley E.
print("Olá Mundo!\n")
# Codigo sem funcões

# Calculadora sem funçoes

# num1 = float (input ( "1° Numero: "))
# num2 = float (input("2°Numero: "))

# soma = num1 + num2
# subtracao = num1 - num2
# multiplicacao = num1 * num2
# divisao = num1 / num2

# print(f"O resultado da soma é: {soma}")
# print(f"O resultado da subtração é: {subtracao}")
# print(f"O resultado da multiplicação é: {multiplicacao}")
# print(f"O resultado da divisão é: {divisao}")

# n1 = float(input('Digite o primeiro valor: '))
# n2 = float(input('Digite o segundo valor: '))

# # # Criando a função para realizar os cálculos
# def calculos (a, b):
#     soma = a + b
#     subtracao  = a - b
#     mutiplicacao = a * b
#     divisao= a / b

#     print("O resultado da soma é: ",soma)
#     print("O resultado da subtração é: ",subtracao)
#     print("O resultado da mutiplicação é: ",mutiplicacao)
#     print("O resultado da divisão é: ",divisao)


# # Chamando a função
# calculos(n1, n2)


# Area do quadrado
largura = float(input('Insira a largura em metros: '))
altura = float (input('Insira a altura em metros: '))

def area(L, C):
 return L * C
print (f'A área do seu quadrado é de:\n {area(largura, altura)} M²')

# Area do triangulo
def area_tri(a, b):
 return (a * b)/ 2
print(f'\nA área do seu triangulo é de:\n {area_tri(largura, altura)} M²')
