# Autor: Wisley
# Projeto Dicionarios

# Detalhes do trabalhador

trabalhador = { 'nome' : 'Nilton', 
               'idade' : 35.0, 
               'salario' : 3500.0, 
               'profissao' : 'desenvolvedor'}
print(f"O tabalhador {trabalhador['nome']} tem a profissão de {trabalhador['profissao']}.\n")

# Exercicio 2
estoque = {"teclado": 10, "mouse": 25, "monitor": 5}
estoque ["teclado"] = 8
estoque ["headset"] = 15

print(f'{estoque}\n')

# Exercicio 3
 
boletim = {'Matematica' : 8., 
           'Historia' : 9.5,
            'Geografia' : 7.,
            'Artes' : 10. ,
            'Portugues' : 6. }
media = sum(boletim.values()) / len(boletim)
print(f'A média do aluno é: {media:.2f}')

# Exercicio 4
usuarios_sistema = {'Wisley' : 'WS123',  'Matheus' : 'MT456',  'Marco' : 'MC789'}
login = input('Digite o usuario: ')
if login in usuarios_sistema:
     senha = input('Digite a senha: ')
     if senha == usuarios_sistema[login]:
      print('Acesso permitido!')
     else:
      print('Senha incorreta')
else:
  print('Usuario não encontrado')
