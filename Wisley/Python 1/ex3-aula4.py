#Autor: Wisley E.
# lista com input


compras = []
for i in range (3):
 produtos = input(f'Digite o {i+1}° produto: ')
 compras.append(produtos)
 print('\nSua lista de compras é: ')
 print(compras)


