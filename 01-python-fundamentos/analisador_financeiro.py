"""
Analisador de Gastos Pessoais
"""

transacoes = [
    {"descricao": "Aluguel", "valor": 1500, "tipo": "despesa"},
    {"descricao": "Salário", "valor": 3000, "tipo": "receita"},
    {"descricao": "Mercado", "valor": 450, "tipo": "despesa"},
    {"descricao": "Freelance", "valor": 800, "tipo": "receita"},
    {"descricao": "Academia", "valor": 120, "tipo": "despesa"}
]


saldo = 0
for t in transacoes:
    if t["tipo"] == "receita":
        saldo += t["valor"]
    else:
        saldo -= t["valor"]


despesas = [t for t in transacoes if t["tipo"] == "despesa"]
maior_despesa = max(despesas, key=lambda d: d["valor"])


media_gastos = sum(d["valor"] for d in despesas) / len(despesas)
print("📊 Analisador Financeiro Pessoal")

print(f"💰 Saldo total: R$ {saldo:.2f}")
print(f"📉 Maior despesa: {maior_despesa['descricao']} - R$ {maior_despesa['valor']:.2f}")
print(f"📊 Média de gastos: R$ {media_gastos:.2f}")
