import pandas as pd 
# Install Openpyxl

df = pd.read_excel('dados_funcionarios.xlsx', engine='openpyxl')

resultado = df.groupby(["Registro", "Nome", "Atividades"])["Horas"].sum()

for (registro, nome, atividades), horas in resultado.items():
    print(f"{registro} - {nome} - {horas} horas de {atividades}")
