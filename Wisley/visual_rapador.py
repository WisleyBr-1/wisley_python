import customtkinter as ctk
from selenium import webdriver as wdv
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import threading
import time

# Configurações de aparência do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AppScraper(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Scraper de Livros Pro")
        self.geometry("600x500")

        # --- Elementos da Interface ---
        self.label_titulo = ctk.CTkLabel(self, text="Web Scraping Visual", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        self.btn_iniciar = ctk.CTkButton(self, text="Iniciar Captura de Dados", command=self.iniciar_thread,
            width=200,        # Largura definida para caber o texto
            height=45,        # Altura maior para centralizar verticalmente
            font=("Roboto", 14, "bold"), # Fonte clara
            corner_radius=10  # Bordas arredondadas
        )
        self.btn_iniciar.pack(pady=10)

        # Caixa de texto para mostrar os resultados
        self.txt_resultado = ctk.CTkTextbox(self, width=500, height=250, font=("Consolas", 12))
        self.txt_resultado.pack(pady=20, padx=20)

        self.status_label = ctk.CTkLabel(self, text="Status: Aguardando...", text_color="gray")
        self.status_label.pack(pady=10)

    def logs(self, mensagem):
        """Função auxiliar para escrever no campo de texto da interface"""
        self.txt_resultado.insert("end", mensagem + "\n")
        self.txt_resultado.see("end")

    def iniciar_thread(self):
        """Inicia o scraping em uma thread separada para não travar a janela"""
        threading.Thread(target=self.executar_scraping, daemon=True).start()

    def executar_scraping(self):
        # Desativa o botão e limpa o texto
        self.btn_iniciar.configure(state="disabled")
        self.txt_resultado.delete("1.0", "end")
        self.status_label.configure(text="Status: Abrindo Navegador...", text_color="#3b8ed0")

        try:
            # Configuração do Selenium
            servico = Service(ChromeDriverManager().install())
            # Opção para não abrir a janela do navegador (opcional):
            # options = wdv.ChromeOptions()
            # options.add_argument("--headless") 
            navegador = wdv.Chrome(service=servico)

            self.logs("Acessando o site alvo...")
            navegador.implicitly_wait(5)
            navegador.get("https://books.toscrape.com")
            time.sleep(2)

            self.status_label.configure(text="Status: Extraindo Dados...")
            self.logs("Buscando informações...")

            # Extração (usando sua lógica original)
            logo = navegador.find_element(By.XPATH, "/html/body/header/div/div/div/a").text
            logo2 = navegador.find_element(By.XPATH, "/html/body/header/div/div/div/small").text

            livro1 = navegador.find_element(By.XPATH, "/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a").text
            livro2_txt = navegador.find_element(By.XPATH, "/html/body/div/div/div/div/section/div[2]/ol/li[14]/article/h3/a").text

            preco1_txt = navegador.find_element(By.XPATH, "/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/div[2]/p[1]").text
            preco2_txt = navegador.find_element(By.XPATH, "/html/body/div/div/div/div/section/div[2]/ol/li[14]/article/div[2]/p[1]").text

            # Exibindo na Interface
            self.logs("="*30)
            self.logs(f"SITE: {logo} - {logo2}")
            self.logs("="*30)
            self.logs(f"LIVRO 1: {livro1}")
            self.logs(f"PREÇO 1: {preco1_txt}")
            self.logs("-" * 20)
            self.logs(f"LIVRO 2: {livro2_txt}")
            self.logs(f"PREÇO 2: {preco2_txt}")
            self.logs("="*30)

            navegador.quit()
            self.status_label.configure(text="Status: Concluído com Sucesso!", text_color="green")

        except Exception as e:
            self.logs(f"ERRO: {str(e)}")
            self.status_label.configure(text="Status: Erro na execução", text_color="red")
        
        finally:
            self.btn_iniciar.configure(state="normal")

if __name__ == "__main__":
    app = AppScraper()
    app.mainloop()