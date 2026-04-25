# Autor: Wisley E.

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
root.geometry("800x500")
root.title("Listas")

lista_aluno = []
'''Criando lista vazia para guardar os nomes '''

def registro_aluno ():
    nome = nome_entry.get()

    if nome != "":
        lista_aluno.append(nome)
        texto_exibicao = "\n".join(lista_aluno)
        # Atualizando o rotulo na tela com a lista nova
        # rotulo.lista.configure(text=f"Alunos presentes: \n {texto_exibicao}")
        # Limpando a caixa de entrada para o proximo nome
        nome_entry.delete(0, "end")

tutulo_label = ctk.CTkLabel(root, )
nome_entry = ctk.CTkEntry(root, placeholder_text="Digite o nome do aluno(a): ")
nome_entry.pack(pady=10)

root.mainloop()