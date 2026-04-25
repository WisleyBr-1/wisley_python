# Autor: Wisley E.
# Projeto funções/temperatura

def temperatura(celsius):
    return (celsius*1.8)+32
def temperaturak(celsius):
    return celsius+273.15
c = float(input('Digite a temperatura: '))
print (f'A temperatura em Fahrenheit é: {temperatura(c)} \ne em Kelvin é: {temperaturak(c)}')
