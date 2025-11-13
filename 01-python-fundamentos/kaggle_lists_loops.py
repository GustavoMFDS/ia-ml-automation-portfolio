"""
DIA 3: Lists, Loops e manipulação de dados
"""

# Trabalhando com listas
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Filtrar apenas números pares
pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", pares)

# 2. Dobrar cada número
dobrados = [num * 2 for num in numeros]
print("Números dobrados:", dobrados)

# 3. Trabalhando com dicionários
transacoes = [
    {"descricao": "Aluguel", "valor": 1500, "categoria": "moradia"},
    {"descricao": "Mercado", "valor": 450, "categoria": "alimentacao"},
    {"descricao": "Salário", "valor": 3000, "categoria": "receita"}
]

# 4. Somar gastos por categoria
total_gastos = 0
for transacao in transacoes:
    if transacao["categoria"] != "receita":
        total_gastos += transacao["valor"]

print("Total de gastos:", total_gastos)