# Autor: Wisley E.
# Projeto: Condicional \n sep end

print('Hoje é sabado', end='!')

print('\nHoje', 'é', 'sabado', sep='_')

print('\n----Sistema de Média Escolar----')

media= float(input('Média: '))

# Condições: Se a média for >= a 5 aluno aprovado
# do contrario aluno reprovado.

if media < 5:
    print('Reprovado')
elif media >=5 and media <7:
    print('Recuperação')
else:
    print('Aprovado')

# média < 5 reprovado
# média >=5 e <7 recuperação
# elif | and
# média >=7 aprovado
