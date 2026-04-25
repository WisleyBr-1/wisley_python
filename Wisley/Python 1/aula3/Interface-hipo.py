# autor Wisley E.
# Projeto: interface gráfica

# Importar a biblioteca
import customtkinter 

# criação da aparência
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Parâmetros da janela
rootinterface = customtkinter.CTk()
rootinterface.geometry('800x400')
rootinterface.title('Sistema Hipotenusa')
rootinterface.resizable(False,False)

# Calculo da área
def calc(): 
 
 cat1 = float(largura_label.get())
 cat2 = float(comprimento_label.get())
 hip = (cat1 **2 + cat2 **2)**0.5
 resultado_label.configure(text=f'A hipotenusa é: {hip}')
 print('eu calculei', hip)
 pass


# Label
labelintro = customtkinter.CTkLabel(rootinterface , text = 'Calculo de Hipotenusa')
labelintro.pack(padx=10, pady=10)

# Entrada 
largura_label = customtkinter.CTkEntry(rootinterface, placeholder_text = ('Altura: '))
largura_label.pack(padx=10, pady=10)
comprimento_label = customtkinter.CTkEntry(rootinterface, placeholder_text= ('Largura: '))
comprimento_label.pack(padx=10, pady=10)


# Botão
resultado_button = customtkinter.CTkButton(rootinterface, text = 'Calcular', command=calc)
resultado_button.pack(padx=8, pady=8)

# Resultado label
resultado_label = customtkinter.CTkLabel(rootinterface, text='')
resultado_label.pack(padx=10, pady=10)

# Renderizar a janela
rootinterface.mainloop()
