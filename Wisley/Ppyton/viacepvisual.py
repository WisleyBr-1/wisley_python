# Autor: Wisley E.
# Projeto: viaCEP com Interface Grafica

# Importação das Bibliotecas
import requests
import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

rootinterface = ctk.CTk()
rootinterface.geometry('900x680')
rootinterface.title('API ViaCEP')

rootinterface.grid_columnconfigure(0, weight=1)
rootinterface.grid_rowconfigure((0, 1, 2), weight=1)

def fcep():
    cep= url_entry.get()
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta= requests.get(url)
    dados = resposta.json()
    if "erro" in dados:
        resultado_label.configure (text=(f'CEP não encontrado'), text_color = "red")  # noqa: F541
    else:
        resultado_label.configure (text=(f'Logradouro: {dados["logradouro"]}\nBairro: {dados["bairro"]}\nCidade: {dados['localidade']}\nUF: {dados['uf']}\nDDD: {dados["ddd"]}'),
                                    text_color="green")

labelintro = ctk.CTkLabel(rootinterface , text = 'CÉPI', text_color='pink', font=('arial', 50, 'bold'))
labelintro.pack(padx=10, pady=50, anchor='center')

url_entry = ctk.CTkEntry(rootinterface, placeholder_text= ('Digite o CEP: '), fg_color="white", text_color="black", width=200, height=35)
url_entry.pack(padx=10, pady=10, anchor='center')
url_entry.bind("<Return>", lambda event: fcep())

resultado_button = ctk.CTkButton(rootinterface, text = 'Consultar', command=fcep, fg_color='purple', font= ("arial", 17, 'bold'), width=150, height=30)
resultado_button.pack(padx=10, pady=10, anchor='center')

# resultado label
resultado_label = ctk.CTkLabel(rootinterface, text='')
resultado_label.pack(padx=10, pady=10, anchor='center')



rootinterface.mainloop()