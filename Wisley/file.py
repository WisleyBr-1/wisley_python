# Escrever em arquivos
# Comando para ler e escrever em arquivos
'''
with open(file="caminho do arquivo", mode="Modo de leitura ou escrita", 
 encode(utf-8)) as apelido:
     bloco de codigo
'''
nome_arquivo = 'pepsico.txt'
with open(file = nome_arquivo, 
          mode=  'w', 
          encoding = 'utf-8') as arquivo:
    print(f'''       Em 1992, nas Filipinas, ocorreu o Incidente 349, uma promoção da Empresa Pepsi,
    se tornou um desastre, Tampinhas premiadas com numeros diarios resultariam em um grande premio. 
        Em 25 de maio o numero 349 foi anunciado como vencedor,
    mas um erro de programação fez com que inúmeras tampinhas tivessem esse numero.''', file = arquivo)