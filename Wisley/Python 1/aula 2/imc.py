altura = float(input("Altura: "))
peso = float(input('Peso: '))

imc = peso/(altura**2)
print(f'Seu IMC é: {imc}')

if imc <18.5:
    print('Você está magro(a)')
elif imc >= 18.5 and imc <25:
    print('Você está com o peso bom!')
elif imc >=25 and imc <30:
    print('Você está com sobrepeso')
elif imc >=30 and imc <35:
    print('Você está com obesidade grau 1')
elif imc >=35 and imc < 40:
    print('Você está com obesidade grau 2')
else:
    print('você esta com Obesidade Grau 3')