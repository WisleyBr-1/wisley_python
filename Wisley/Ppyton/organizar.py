# Autor: Wisley E.
# Projeto: Renomear arquivos

# Importar ação do OS(Sistema operacional - windows)
import os

folder = 'files'

# Listar arquivos das pastas
list_files = os.listdir(folder)

# Loop dos arquivos
contador = 1

for file in list_files:
 
# um arquivo tem nome e extensão
# separar o nome da extensão
# boleto_a1327_2026.pdf
    name, extension = os.path.splitext(file)

# Geração  do novo nome
    new_name = (f'Elpepeee_Ronaldo{contador:03d}{extension}')

# Caminho do arquivo antigo
    caminho_antigo = os.path.join(folder, file)

# Caminho do novo arquivo
    caminho_novo = os.path.join(folder, new_name)

# Ação de renomear os arquivos
    os.rename(caminho_antigo, caminho_novo)



# Mensagem de sucesso
    print(f"Arquivo {file} renomeado para {new_name}")

    contador += 1


print("\nTodos os arquivos foram renomeados com sucesso")