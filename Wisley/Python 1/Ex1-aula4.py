# Autor: Wisley E.
# Exercicio 1 da aula 4

print()
alunos = ['Marco','Matheus', "Enzo", 'Cleber', "Mario"]
print(f'{alunos}\n')

alunos.extend (['Wisley', 'Andre', 'João'])
print(alunos)
print(f"{len(alunos)} alunos\n")

alunos.insert(0, 'Alvaro')
print(alunos)
