# autor: Wisley E.
# Projeto: interface gráfica

# Importar a biblioteca
import customtkinter 

# criação da aparência
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Parâmetros da janela
rootinterface = customtkinter.CTk(fg_color="black")
rootinterface.geometry('800x400')
rootinterface.title('Sistema IMC')
rootinterface.resizable(False,False)

# Calculo do IMC
def calc(): 
 
 altura = float(altura_label.get())
 peso = float(peso_label.get())
 imc = peso/(altura**2)

 if imc <18.5:
     classificacao = 'Magreza'
 elif imc >= 18.5 and imc <25:
     classificacao = 'Peso Normal'
 elif imc <30:
     classificacao = 'Sobrepeso'
 elif imc <35:
     classificacao = 'Obesidade Grau 1'
 elif imc < 40:
     classificacao = 'Obesidade Grau 2'
 else:
     classificacao = 'Obesidade Grau 3'

 resultado_label.configure(
     text=f'Olá {nome_label.get()} seu IMC é: {imc:.2f}. \n{classificacao}',
     text_color='pink', font=('arial', 12, 'bold'))

 print(classificacao)
# Label
labelintro = customtkinter.CTkLabel(rootinterface , text = 'Calculadora de IMC', text_color="Purple", font=("Arial", 15, 'bold'))
labelintro.pack(padx=10, pady=10)
# Entrada 
nome_label = customtkinter.CTkEntry(rootinterface, placeholder_text= ('Nome: '), fg_color="white", text_color="black")
nome_label.pack(padx=10, pady=10)

altura_label = customtkinter.CTkEntry(rootinterface, placeholder_text = ('Altura em metros: '), fg_color='white', text_color='black')
altura_label.pack(padx=10, pady=10)

peso_label = customtkinter.CTkEntry(rootinterface, placeholder_text= ('Peso em kilos: '), fg_color='white', text_color='black')
peso_label.pack(padx=10, pady=10)


# Botão
resultado_button = customtkinter.CTkButton(rootinterface, text = 'Calcular', command=calc, fg_color='purple', font= ("arial", 15, 'bold'))
resultado_button.pack(padx=8, pady=8)

# resultado label
resultado_label = customtkinter.CTkLabel(rootinterface, text='')
resultado_label.pack(padx=10, pady=10)


# Renderizar a janela
rootinterface.mainloop()
