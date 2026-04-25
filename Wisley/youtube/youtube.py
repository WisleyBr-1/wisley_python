# Autor: Wisley E.
# Projeto: Sistema
# Download de videos youtube

# Importar a biblioteca
import customtkinter
from pytubefix import YouTube
from pytubefix.cli import on_progress

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

rootinterface = customtkinter.CTk()
rootinterface.geometry('800x400')
rootinterface.title('Baixador de videos')
rootinterface.resizable(False,False)

def byt():
    yt = YouTube(url_label.get(), on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()
    resultado_label.configure (text='Baicandoo...', text_color="yellow", font=('arial', 15 , 'bold'))
    ys.download()  
    resultado_label.configure (text='Baka! Seu download foi concluido', text_color="yellow", font=('arial', 15 , 'bold'))

labelintro = customtkinter.CTkLabel(rootinterface , text = 'Downtube do Wix', text_color='pink', font=('arial', 17, 'bold'))
labelintro.pack(padx=30, pady=30)

url_label = customtkinter.CTkEntry(rootinterface, placeholder_text= ('Digite a url: '), fg_color="white", text_color="black")
url_label.pack(padx=10, pady=10)

resultado_button = customtkinter.CTkButton(rootinterface, text = 'Baixar', command=byt, fg_color='purple', font= ("arial", 15, 'bold'))
resultado_button.pack(padx=8, pady=8)

# resultado label
resultado_label = customtkinter.CTkLabel(rootinterface, text='')
resultado_label.pack(padx=10, pady=10)



rootinterface.mainloop()

