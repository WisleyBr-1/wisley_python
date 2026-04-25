# Autor : Wisley E.
# Projeto: Consumo de API
import requests

cep= input('Digite o CEP: ')
url = f"https://viacep.com.br/ws/{cep}/json/"
resposta= requests.get(url)
dados = resposta.json()
if "erro" in dados:
 print('CEP não encontrado')
else:
 print(f'''Logradouro: {dados["logradouro"]} 
                Bairro: {dados["bairro"]}
                Cidade: {dados['localidade']}
                UF: {dados['uf']}
                DDD: {dados["ddd"]}''')

