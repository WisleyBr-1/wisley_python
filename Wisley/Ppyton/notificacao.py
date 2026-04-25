# Autor: Wisley E.
# Projeto: Notificações

import requests as req

topico = "wisleye"

nome = input("Digite seu nome: ")

url = f"https://ntfy.sh/{topico}"

req.post(url, 
         data= f"{nome} acabou de te mandar um salve!".encode('utf-8')
         )
print("Mensagem enviada!!😘")