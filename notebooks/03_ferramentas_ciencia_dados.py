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
# Módulo 3: Ferramentas Essenciais de Ciência de Dados (NumPy e Pandas)

# Documentação: Importando a biblioteca NumPy
import numpy as np

# 1. Criação de um Array (Vetor 1D)
dados_vendas = [100, 250, 400, 120] # Lista Python
vendas_array = np.array(dados_vendas) # Array NumPy

print(f"Lista Python: {dados_vendas}")
print(f"Array NumPy: {vendas_array}")

# 2. Operações em Massa: Aplicando um aumento de 10% em todas as vendas
aumento_percentual = 0.10
vendas_com_aumento = vendas_array * (1 + aumento_percentual)

print("\n---")
# A operação de multiplicação foi aplicada a CADA elemento do array, de uma vez!
print(f"Vendas com aumento de 10%: {vendas_com_aumento}")

# 3. Funções Úteis: Cálculo rápido de estatísticas
media_vendas = np.mean(vendas_array)
print(f"Média das vendas originais: R${media_vendas:.2f}")

# %%
# Documentação: Importando a biblioteca Pandas
import pandas as pd

# Reutilizando a sua lista de dicionários do Módulo 2
registro_vendas = [
    {"item": "Laptop", "quantidade": 1, "valor_unitario": 5000.99},
    {"item": "Mouse", "quantidade": 10, "valor_unitario": 299.99},
    {"item": "Teclado", "quantidade": 5, "valor_unitario": 499.99},
]

# 1. Criação do DataFrame
df_vendas = pd.DataFrame(registro_vendas)

# 2. Exibindo o DataFrame (O Jupyter mostra isso como uma tabela formatada!)
print("Seu DataFrame (Tabela de Dados):")
print(df_vendas)

# 3. Adicionando uma nova coluna (Processamento de Dados)
# O Pandas, assim como o NumPy, aplica a multiplicação em todos os valores da coluna
df_vendas['valor_total'] = df_vendas['quantidade'] * df_vendas['valor_unitario']

# 4. Análise Rápida: Exibindo a média da coluna 'valor_unitario'
media_unitario = df_vendas['valor_unitario'].mean()

print("\n---")
print("DataFrame com coluna 'valor_total' adicionada:")
print(df_vendas)
print(f"\nMédia do valor unitário: R${media_unitario:.2f}")

# %%
# Exercício de Fixação do Módulo 3: Prática com Pandas
# Desafio:
# Use o df_vendas (o DataFrame que você acabou de criar).
# Filtre o DataFrame para mostrar apenas as vendas onde a 'quantidade' é maior que 5.
# Imprima o resultado desse filtro.

# Documentação: filtragem do DataFrame e impressão do resultado do filtro
filtered_df = df_vendas[df_vendas['quantidade'] > 5]
print(filtered_df)

# %%
# Documentação: Carregar e Limpar Dados
import pandas as pd
import numpy as np

# Dados simulados com valores ausentes (NaN)
dados = {
    'Marca': ['Toyota', 'Honda', 'Ford', 'Tesla', 'Chevrolet', 'BMW'],
    'Modelo': ['Corolla', 'Civic', 'Fusion', 'Model 3', 'Cruze', 'X1'],
    'Preco': [25000, 32000, np.nan, 55000, 21000, 48000], # Preço do Fusion está ausente
    'Ano': [2018, 2020, 2017, 2022, 2019, np.nan],        # Ano do BMW está ausente
    'Quilometragem': [50000, 30000, 65000, 15000, 40000, 20000]
}

# Cria o DataFrame e salva como CSV
df_exemplo = pd.DataFrame(dados)
df_exemplo.to_csv('../data/raw/carros.csv', index=False) # index=False evita salvar o índice como coluna

print("Arquivo 'carros.csv' criado com dados de exemplo e ausentes.")

# %%
# Documentação: Carregando o arquivo e visualizando as primeiras linhas.

# Carrega o arquivo CSV em um novo DataFrame
df_carros = pd.read_csv('../data/raw/carros.csv')

print("--- DataFrame Carregado (As primeiras 5 linhas) ---")
# .head() mostra as primeiras 5 linhas
print(df_carros.head()) 

print("\n--- Informações sobre o DataFrame (Missing Data) ---")
# .info() é crucial para ver o tipo de dado de cada coluna e quantos valores não-nulos existem
df_carros.info()

# %%
# Documentação: Removendo todas as linhas que contêm pelo menos um valor NaN (Not a Number).
# OBS.: código comentado para reforçar aprendizado mas sem executar, por não ser objetivo neste momento.

# Cria um novo DataFrame apenas com as linhas COMPLETAS
#df_limpo_dropna = df_carros.dropna()

#print("\n--- DataFrame após a remoção de linhas incompletas ---")
#print(df_limpo_dropna) 
#print(f"\nTamanho original: {len(df_carros)} linhas. Tamanho limpo: {len(df_limpo_dropna)} linhas.")

# %%
# Documentação: Preenchendo valores NaN com a média da coluna.

# 1. Calculando a média da coluna 'Preco' (apenas para valores não-nulos)
media_preco = df_carros['Preco'].mean()
print(f"Média do preço calculado: R${media_preco:.2f}")

# 2. Preenchendo os valores NaN na coluna 'Preco' com essa média
# .fillna(valor, inplace=True) altera o DataFrame original
df_carros['Preco'].fillna(media_preco, inplace=True)

print("\n--- Preenchimento concluído (Preço do Fusion agora é a média) ---")
print(df_carros)

# %%
# Documentação: Correção do erro de conversão de tipo de dado.

# 1. Aplicar .round(0) para garantir que todos os valores float terminem em .0
# Isso torna a conversão para int "segura".
df_carros['Ano'] = df_carros['Ano'].round(0)

# 2. Agora, convertemos para o tipo Int64 (o que suporta NaN)
# O erro TypeError não deve ocorrer mais.
df_carros['Ano'] = df_carros['Ano'].astype('Int64') 

# 3. Calculamos a média (que agora será uma média de Int64) e preenchemos.
# Usamos .floor() do numpy para arredondar para baixo, garantindo que seja um ano válido.
# Importante: Como agora a coluna é Int64, .mean() pode retornar float, por isso o int() é mantido.
media_ano = int(np.floor(df_carros['Ano'].mean())) 

print(f"Média do ano calculado (arredondado): {media_ano}")

# 4. Preencher o valor faltante (NaN) com a média inteira
df_carros['Ano'].fillna(media_ano, inplace=True)

print("\n--- Preenchimento concluído e tipo de dado corrigido ---")
print(df_carros)

# 5. Verificando o tipo da coluna 'Ano' (deve ser Int64)
print("\nVerificação do Tipo de Dado (DTYPE):")
df_carros.info()

# %%
