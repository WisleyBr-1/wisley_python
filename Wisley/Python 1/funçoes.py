# Autor: Wisley E.
# Projeto com funções

# Criação da função
def triangulo(base, altura):
    return (base * altura) / 2

b = float(input('Base: '))
a = float(input('Altura: '))
print(f'A area do trinagulo é: {triangulo(b,a)}')