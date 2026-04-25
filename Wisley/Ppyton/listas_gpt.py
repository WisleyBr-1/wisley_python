import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x550")
root.title("Lista de Compras")

compras = []

# ====== FUNÇÕES ======

def atualizar_lista():
    for widget in frame_lista.winfo_children():
        widget.destroy()

    for item in compras:
        item_frame = ctk.CTkFrame(frame_lista, corner_radius=10)
        item_frame.pack(fill="x", pady=6, padx=5)

        label = ctk.CTkLabel(
            item_frame,
            text=item,
            font=("Arial", 16)
        )
        label.pack(side="left", padx=15, pady=10)

        botao_remover = ctk.CTkButton(
            item_frame,
            text="✖",
            width=35,
            height=30,
            corner_radius=8,
            fg_color="#ff4d4d",
            hover_color="#cc0000",
            command=lambda i=item: remover_item(i)
        )
        botao_remover.pack(side="right", padx=10)

def adicionar():
    texto = entry.get().strip()

    if texto != "":
        compras.append(texto)
        atualizar_lista()

    entry.delete(0, "end")

def remover_item(item):
    compras.remove(item)
    atualizar_lista()

# ====== UI ======

titulo = ctk.CTkLabel(
    root,
    text="🛒 Lista de Compras",
    font=("Arial", 28, "bold")
)
titulo.pack(pady=20)

# linha de input + botão
frame_input = ctk.CTkFrame(root, fg_color="transparent")
frame_input.pack(pady=10)

entry = ctk.CTkEntry(
    frame_input,
    placeholder_text="Digite um item...",
    width=250,
    height=40,
    corner_radius=10
)
entry.pack(side="left", padx=10)
entry.bind("<Return>", lambda event: adicionar())

botao_add = ctk.CTkButton(
    frame_input,
    text="Adicionar",
    width=120,
    height=40,
    corner_radius=10,
    command=adicionar
)
botao_add.pack(side="left")

# lista
frame_lista = ctk.CTkScrollableFrame(
    root,
    width=450,
    height=350,
    corner_radius=10
)
frame_lista.pack(pady=20)

root.mainloop()