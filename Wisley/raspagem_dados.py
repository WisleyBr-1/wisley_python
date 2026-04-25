
# ===================================================================
# HELLO WORLD DO SELENIUM — Seu Primeiro Robô
# Protocolo de Iniciação: Abrir navegador, acessar site, encerrar.
# ===================================================================

# IMPORTAÇÕES — O Arsenal do Robô
from selenium import webdriver                          # Motor principal: controla o navegador
from selenium.webdriver.chrome.service import Service    # Gerencia o serviço do Chrome no Windows
from webdriver_manager.chrome import ChromeDriverManager # O "gerente de infraestrutura"
from selenium.webdriver.common.by import By
import time                                              # Controle de tempo (pausas)

# ===================================================================
# PASSO 1 — Configura o driver automaticamente
# O ChromeDriverManager é o nosso "gerente de infraestrutura".
# Ele verifica qual versão do Chrome você tem instalada,
# baixa o chromedriver correto e configura tudo sozinho.
# Sem ele, você teria que fazer isso manualmente toda vez
# que o Chrome atualizasse. Deploy automático!
# ===================================================================
servico = Service(ChromeDriverManager().install())

# ===================================================================
# PASSO 2 — Abre o navegador Google Chrome
# O webdriver.Chrome() inicia uma nova janela do Chrome.
# O parâmetro service=servico conecta ao driver correto.
# A partir daqui, a variável 'navegador' é o seu controle remoto.
# ===================================================================
navegador = webdriver.Chrome(service=servico)

# ===================================================================
# PASSO 3 — Aguarda 3 segundos com o navegador aberto (e vazio)
# O time.sleep(3) pausa a execução por 3 segundos.
# Serve para você VER que o Chrome abriu antes de navegar.
# Na automação, pausas respeitam a latência da rede.
# ===================================================================
print("Navegador aberto. Aguardando 3 segundos...")
time.sleep(3)

# ===================================================================
# PASSO 4 — Acessa o site escolhido
# O .get() é como digitar a URL na barra e pressionar Enter.
# Aqui estamos acessando o site oficial do SENAI SP.
# ===================================================================
print("Acessando o site...")
navegador.get("https://g1.globo.com/")

manchete = navegador.find_element(By.XPATH,"/html/body/div[2]/main/div[2]/div/div/div/div/div[1]/div/a/ul/li[5]/div/div/span").text
# ===================================================================
# PASSO 5 — Aguarda 5 segundos para que todos vejam o site carregado
# Essa pausa é proposital: dá tempo para o site renderizar
# completamente e para você confirmar visualmente que funcionou.
# Em redes corporativas com latência alta, essa pausa é essencial.
# ===================================================================
time.sleep(5)

# ===================================================================
# PASSO 6 — Encerra o navegador de forma controlada
# O .quit() fecha TODAS as janelas do Chrome abertas pelo Selenium
# e encerra o processo no Gerenciador de Tarefas.
# Sem isso, o Chrome ficaria aberto consumindo memória.
# Governança de recursos!
# ===================================================================
navegador.quit()
print(manchete)
print("Teste finalizado com sucesso! 🏁")
