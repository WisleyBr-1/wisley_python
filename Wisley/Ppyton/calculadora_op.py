
def calcular(a, b, op):
    return eval(f'{a}{op}{b}')

n1= float(input("1° Numero: "))
n2= float(input("2° Numero: "))
op = input('Escolha a operação (+ - * /): ')

print("Resultado", calcular(n1, n2, op))