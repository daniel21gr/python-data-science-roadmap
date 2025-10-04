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
# Módulo 1: Fundamentos do Python

# Documentação: Definindo variáveis para o nosso cálculo.

# Variável 'str' (texto) para identificar o que estamos calculando
nome_do_projeto = "Cálculo de Área"

# Variável 'int' (inteiro) que representa o lado do nosso quadrado
lado_do_quadrado = 5

# %%
# Documentação: Realizando a operação matemática.

# A área é calculada multiplicando o lado por ele mesmo.
# O resultado da expressão (5 * 5) é atribuído à variável 'area'.
area_do_quadrado = lado_do_quadrado * lado_do_quadrado

# %%
# Documentação: Exibindo os resultados usando a função print().

print(nome_do_projeto)
print("---") # Imprime uma linha separadora

# Imprime o texto e o valor da variável 'area_do_quadrado'
print("A área calculada é:", area_do_quadrado)

# Você também pode usar a variável diretamente para mostrar o valor na última célula do Jupyter
# area_do_quadrado

# %%
# Exercício de Fixação

# Desafio:
# Crie uma nova célula (ou modifique a Célula 1).
# Crie uma variável chamada raio e atribua a ela o valor 7.5 (Este é um número float).
# Crie outra variável chamada PI e atribua o valor 3.14159 a ela.
# Crie uma variável chamada circunferencia e use a fórmula:
#     Circunferência=2×PI×raio
# Use a função print() para exibir o valor de circunferencia.

# Documentação: Definindo variáveis para o cálculo.
nome_do_projeto = "Cálculo de Circunferência"

raio = 7.5
pi = 3.14159

# %%
# Documentação: Realizando operação matemática.

circunferencia = 2 * pi * raio

# %%
# Documentação: Exibindo resultados usando a função print().

print(nome_do_projeto)
print("---")

print("Circunferência é:", circunferencia)

# %%
