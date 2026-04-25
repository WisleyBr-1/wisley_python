# Autor: Wisley E.
# Projeto: Aprendendo listas em python.
# Listas são mutaveis

print()
nomes = ['Wisley' , 'Matheus' , 'Marco'] 
print(nomes)

# Adicionando nomes na lista

nomes.append('Enzo')
print(f"Adicionando nomes na lista com append:  {nomes}\n")

# Utlilizando o insert em uma lista
nomes.insert(1, "han")
print(f"Alterando a lista com inser: {nomes}\n")

# Utilizando o extend em uma lista
nomes.extend(["Epstein", 'Sim'])
print(f"adicionando uma lista com extend:  {nomes}\n")
print(f"{nomes[1]}, {nomes[0]}, {nomes[3]})")


notas = [0] * 7
print(f'Maior: {max(notas)}')
print(f'Menor: {min(notas)}')
print(f'Soma: {sum(notas)}')

media = sum(notas) / len(notas)
print(f"A média é: {media}\n")
soma = 0
x = 0

while x <7:
 notas[x] = float(input(f'Nota {x+1}: '))
 soma+= notas[x]
 x += 1
print(f"Média: {soma / x:.2f}")
    