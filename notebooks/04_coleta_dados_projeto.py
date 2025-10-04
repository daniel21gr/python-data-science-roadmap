# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# Módulo 4: Coleta de Dados e Projeto

# Módulo para fazer requisições HTTP (comunicação web)
import requests
# Módulo essencial para manipulação e análise de dados tabulares
import pandas as pd

# %%
# Documentação: Fazer a requisição GET e converter o JSON.

# Endpoint (URL) da API para buscar comentários do Post ID 1
url_api = "https://jsonplaceholder.typicode.com/posts/1/comments"

# ETAPA A: Fazer a requisição HTTP GET
response = requests.get(url_api)

# ETAPA B: Verificar o Status
# O código 200 significa "OK" (sucesso).
if response.status_code == 200:
    
    # ETAPA C: Converter a resposta JSON em uma Lista de Dicionários Python
    # Essa variável é a base para nossa análise com Pandas!
    dados_comentarios = response.json()
    
    print(f"Sucesso! Dados recebidos. Total de itens: {len(dados_comentarios)}")
    
    # Exibe o primeiro item (que é um Dicionário) para inspeção
    print("\n--- Estrutura do Primeiro Item (Dicionário) ---")
    print(dados_comentarios[0])
    
else:
    print(f"Erro ao acessar a API. Status Code: {response.status_code}")
    dados_comentarios = [] # Garante que a variável exista mesmo em caso de erro

# %%
# Documentação: Análise de dados da web usando o Pandas.

# 1. TRANSFORMAÇÃO: Converta a lista de dicionários em um DataFrame Pandas
df_comentarios = pd.DataFrame(dados_comentarios)

# 2. PROCESSAMENTO: Crie a nova coluna 'tamanho_corpo'
# Use a função de string do Pandas para calcular o comprimento (len) do texto na coluna 'body'6
df_comentarios['tamanho_corpo'] = df_comentarios['body'].str.len()

# 3. ANÁLISE: Calcule e imprima a média e o máximo do 'tamanho_corpo'
media_tamanho = df_comentarios['tamanho_corpo'].mean()
max_tamanho = df_comentarios['tamanho_corpo'].max()

print("\n--- Resultados da Análise de Comentários ---")
print(f"Média do tamanho dos comentários: {media_tamanho:.0f} caracteres")
print(f"Tamanho máximo de um comentário: {max_tamanho} caracteres")

print("\n--- Visualização do Resultado ---")
print(df_comentarios[['name', 'body', 'tamanho_corpo']].head(3))
