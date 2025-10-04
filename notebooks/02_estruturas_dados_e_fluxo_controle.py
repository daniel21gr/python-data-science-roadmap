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
# Módulo 2: Estruturas de Dados e Fluxo de Controle

# Módulo 2.1: Estruturas de Dados Essenciais
# Documentação: Criando e acessando itens em uma Lista.

# 1. Criação da Lista
produtos = ["Laptop", "Mouse", "Teclado", "Monitor", "Webcam"]

# 2. Imprimindo a lista inteira
print("Lista completa de produtos:", produtos)

# 3. Acessando um item: Python usa indexação baseada em ZERO!
# O primeiro item está no índice 0.
primeiro_produto = produtos[0]
print("O primeiro produto (índice 0) é:", primeiro_produto)

# 4. Alterando um item: Listas são MUTÁVEIS.
produtos[4] = "Webcam HD"
print("A lista após a atualização do índice 4:", produtos)

# %%
# Documentação: Criando e acessando dados em um Dicionário.

# 1. Criação do Dicionário
dados_produto = {
    "nome": "Smartphone X",
    "preco": 999.99,
    "em_estoque": True,
    "categorias": ["Eletronicos", "Comunicação"] # Um valor pode ser uma LISTA!
}

# 2. Acessando um Valor pela Chave (não pelo índice!)
preco_do_produto = dados_produto["preco"]
print("O preço do produto é:", preco_do_produto)

# 3. Alterando um Valor
# Mudando o status de estoque
dados_produto["em_estoque"] = False
print("Status de estoque atualizado:", dados_produto["em_estoque"])

# %%
# Exercício de Fixação de Estruturas de Dados Essenciais: O Registro de Vendas

# Desafio:
# Crie uma Lista chamada registro_vendas.
# Dentro desta lista, insira três Dicionários diferentes, onde cada dicionário representa uma venda.
# Estrutura de cada Dicionário:
#    'item': (String) Nome do produto vendido (ex: 'Monitor').
#    'quantidade': (Inteiro) Número de itens vendidos (ex: 2).
#    'valor_unitario': (Float) Preço por item (ex: 250.00).
# Após criar a lista, acesse e imprima a quantidade vendida no segundo registro (a segunda venda da sua lista).

# Documentação: lista de registro de vendas com estrutura pedida
registro_vendas = [
    {
        "item": "Laptop",
        "quantidade": 1,
        "valor_unitario": 5000.99
    },
    {
        "item": "Mouse",
        "quantidade": 10,
        "valor_unitario": 299.99
    },
    {
        "item": "Teclado",
        "quantidade": 5,
        "valor_unitario": 499.99
    },
]

# Documentação: acesso e impressão da quantidade vendida do segundo registro
segundo_item = registro_vendas[1]
print(segundo_item["quantidade"])

# %%
# Módulo 2.2: Fluxo de Controle (Condições e Loops)

# Módulo 2.2.1: Condições e Ramificações (if, elif, else)
# Documentação: Usando 'if', 'elif' e 'else' para tomar decisões.

# Reutilizando seu dado de vendas: vamos focar no primeiro item
primeiro_registro = registro_vendas[0] # Dicionário do "Laptop"
quantidade_atual = primeiro_registro["quantidade"]
nome_item = primeiro_registro["item"]

print(f"Verificando estoque para: {nome_item}. Quantidade: {quantidade_atual}")

if quantidade_atual == 0:
    # Este bloco é executado se a condição for True
    print("ESTOQUE ZERADO! Pedido urgente necessário.")
elif quantidade_atual < 5:
    # Este bloco é executado se a primeira condição for False, mas esta for True
    print("ESTOQUE BAIXO! Reabastecer em breve.")
else:
    # Este bloco é executado se NENHUMA das condições anteriores for True
    print("Estoque suficiente. Tudo certo.")

# %%
# Módulo 2.2.2: Loops (for): Repetição Automatizada
# Documentação: Usando um loop 'for' para processar cada item de uma lista.

# Inicializa uma variável para acumular o total geral
total_geral_vendas = 0

# Loop 'for': 'venda' será o nome da variável temporária que representa cada dicionário
for venda in registro_vendas:
    # 1. Extrai os valores do dicionário atual
    item = venda["item"]
    quantidade = venda["quantidade"]
    valor_unitario = venda["valor_unitario"]

    # 2. Calcula o total da transação
    total_transacao = quantidade * valor_unitario
    
    # 3. Acumula no total geral
    total_geral_vendas = total_geral_vendas + total_transacao

    # 4. Imprime um resumo para a transação atual (opcional)
    print(f"Venda de {item}: {quantidade} x R${valor_unitario:.2f} = R${total_transacao:.2f}")

print("\n---")
print(f"TOTAL GERAL DE VENDAS: R${total_geral_vendas:.2f}")


# %%
# Módulos 2.3: Funções (Reutilizando e Organizando o Código)
# Documentação: Função para calcular a área de um quadrado.

def calcular_area_quadrado(lado):
    """
    Calcula e retorna a área de um quadrado.
    :param lado: O comprimento do lado do quadrado (int ou float).
    :return: A área do quadrado (lado * lado).
    """
    area = lado * lado
    return area # O resultado da área é retornado
    
# --- Chamando a Função (Uso) ---

# 1. Chamando com um valor simples
area1 = calcular_area_quadrado(10) 
print(f"Área de um quadrado com lado 10: {area1}")

# 2. Chamando com outro valor (reutilização)
area2 = calcular_area_quadrado(7.5)
print(f"Área de um quadrado com lado 7.5: {area2}")


# %%
# Documentação: Função para analisar e retornar o status do estoque.

def verificar_status_estoque(item, quantidade_atual, limite_baixo=5):
    """
    Verifica o nível de estoque com base em um limite e retorna uma mensagem.
    :param item: Nome do produto (str).
    :param quantidade_atual: Quantidade em estoque (int).
    :param limite_baixo: Limite para considerar 'estoque baixo'. Padrão é 5.
    :return: Uma string com o status do estoque.
    """
    if quantidade_atual == 0:
        status = f"ALERTA URGENTE: {item} está ZERADO."
    elif quantidade_atual < limite_baixo:
        status = f"ALERTA BAIXO: {item} precisa de reposição."
    else:
        status = f"OK: {item} possui estoque suficiente ({quantidade_atual})."
        
    return status

# --- Chamando a Função ---

# Reutilizando seu registro de vendas
status_mouse = verificar_status_estoque("Mouse", registro_vendas[1]["quantidade"])
print(status_mouse) # Esperado: OK (10 é maior que o padrão 5)

# Testando com o limite baixo
status_teclado = verificar_status_estoque("Teclado", registro_vendas[2]["quantidade"], 8)
print(status_teclado) # Esperado: ALERTA BAIXO (5 é menor que 8)

# %%
