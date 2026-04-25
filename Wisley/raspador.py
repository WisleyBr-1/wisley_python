from selenium import webdriver as wdv # O controle principal do navegador
from selenium.webdriver.chrome.service import Service # Gerencia o serviço de driver do windows
from webdriver_manager.chrome import ChromeDriverManager # Faz o download automatico do driver correto
from selenium.webdriver.common.by import By # Permite localizar os elementos por id, classe ou PATH
import time

# Estrutura
# Config automatica para baixar o driver

servico = Service (ChromeDriverManager().install())
navegador = wdv.Chrome (service = servico)

# Define o tempo de espera
print("Acessando o site alvo...")

navegador.implicitly_wait(5)
navegador.get("https://books.toscrape.com")
time.sleep(2)

print("Buscando o alvo...")

logo = navegador.find_element(By.XPATH, "/html/body/header/div/div/div/a").text
logo2 = navegador.find_element(By.XPATH, "/html/body/header/div/div/div/small").text

livro1 = navegador.find_element(By.XPATH, 
                "/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a").text
livro2_txt = navegador.find_element(By.XPATH, 
                "/html/body/div/div/div/div/section/div[2]/ol/li[14]/article/h3/a").text

preco1_txt = navegador.find_element(By.XPATH, 
                "/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/div[2]/p[1]").text
preco2_txt = navegador.find_element(By.XPATH, 
                "/html/body/div/div/div/div/section/div[2]/ol/li[14]/article/div[2]/p[1]").text

print(f"O Texto extraido foi: {logo} - {logo2}!")
print(f"Livro: {livro1}\n Preço: {preco1_txt}\n \nLivro: {livro2_txt} \nPreço: {preco2_txt}")