# autor: Wisley
# tuplas

# EX 1
# print()
# meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
# print(f"O 3° mês é: {meses[3]} \nO último mês é: {meses[11]} ")

# EX 2
# config = ('Dark', 'Português', 'True')
# config.insert(0, "Light")
# Tuplas são imutaveis, por isso dar erro ao tentar mudar

# EX 3
# ponto_gps =  (-23.5505, -46.6333)
# latidude, longitude = ponto_gps
# print(f'Latitude: {latidude}')
# print(f'Longitude: {longitude}')

# EX 4
# notas = (8.5, 7.0, 9.0, 6.0, 10.0)
# print(f'Maior: {max(notas)}')
# print(f'Menor: {min(notas)}')
# print(f'Soma: {sum(notas)}')

# media = sum(notas) / len(notas)
# print(f"A média é: {media}\n")

# EX 5
# frutas_fixas = ('Maçã', 'Banana')

# lista_frutas = list(frutas_fixas)
# lista_frutas.append('Uva')

# tupla_final = tuple(lista_frutas)
# print(tupla_final)

# Desafio
frutas_fixas = ('Maçã', 'Banana')

lista_frutas = list(frutas_fixas)
fruta = input('Digite a Fruta: ')
lista_frutas.append(fruta)

tupla_final = tuple(lista_frutas)
print(tupla_final)
