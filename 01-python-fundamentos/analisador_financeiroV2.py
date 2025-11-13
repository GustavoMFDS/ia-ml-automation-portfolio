
"""
DIA 3: Versão com menu interativo
"""

transacoes = []

def menu_principal():
    while True:
        print("Analisador Financeiro V2")
        print("1.Adicionar Transação")
        print("2.Ver relátorio")
        print("3.Salvar arquivo")
        print("4.Sair")

        opcao = input("Escolha uma opção")

        if opcao == "1":
            adicionar_transacao()
        elif opcao == "2":
            ver_relatorio()
        elif opcao == "3":
            salvar_arquivo()
        elif opcao == "4":
            print("Fechando")
            break
        else:
            print("Opcao Invalida")
def adicionar_transacao():
    print("Nova transação")
    descricao = input("Descrição: ")
    valor = float(input("Valor: R$"))
    tipo = input("Tipo(Receita/Despesa)")
    
    transacao = {
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
    }
    transacoes.append(transacao)
    print("Transacao '{descricao}' adicionado.")

def ver_relatorio():
    if not transacoes:
     print("Nenhuma transacao cadastrada no sistema")
     return
   
    print("Relatorio")
    for i, transacao in enumerate(transacoes, 1):
        print( f"{i}.{transacao['descricao']}: R$ {transacao['valor']} ({transacao['tipo']})" )

if __name__ == "__main__":
 menu_principal()