# Autor: Wisley E.

import customtkinter

# Aparência
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Janela
rootinterface = customtkinter.CTk()
rootinterface.geometry('800x400')
rootinterface.title('Sistema Area')
rootinterface.resizable(False, False)

# Função de cálculo
def calc():
    largura = float(entry_largura.get())
    comprimento = float(entry_comprimento.get())
        
    area = largura * comprimento
        
    resultado_label.configure(text=f'Área: {area} m²')
    print(area, 'M²')

# Título
labelintro = customtkinter.CTkLabel(rootinterface, text='Cálculo de Área')
labelintro.pack(padx=10, pady=10)

# Entradas
entry_largura = customtkinter.CTkEntry(rootinterface, placeholder_text='Largura em metros')
entry_largura.pack(padx=10, pady=10)

entry_comprimento = customtkinter.CTkEntry(rootinterface, placeholder_text='Comprimento em metros')
entry_comprimento.pack(padx=10, pady=10)

# Botão
resultado_button = customtkinter.CTkButton(rootinterface, text='Calcular', command=calc)
resultado_button.pack(padx=8, pady=8)


# Label de resultado
resultado_label = customtkinter.CTkLabel(rootinterface, text='')
resultado_label.pack(padx=10, pady=10)

# Loop
rootinterface.mainloop()