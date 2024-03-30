MENU = {
    "espresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "custo": 1.5,
    },
    "cafe": {
        "ingredientes": {
            "agua": 200,
            "leite": 150,
            "cafe": 24,
        },
        "custo": 2.5,
    },
    "cappucino": {
        "ingredientes": {
            "agua": 250,
            "leite": 100,
            "cafe": 24,
        },
        "custo": 3.0,
    }
}

custo = 0

recursos = {
    "agua": 300,
    "leite": 200,
    "cafe": 100,
}

def recursos_suficientes(pedido_ingredientes):
    """ Retorna verdadeiro quando o pedido pode ser feito, retorna False se os
     ingredientes estiverem faltando """
    for item in pedido_ingredientes:
        if pedido_ingredientes[item] > recursos[item]:
            print(f"Desculpe, não há {item} suficiente .")
            return False
    return True


def processar_pagamento():
    """ Retorna o total calculado de dinheiro inserido """
    print("Por favor deposite o dinheiro. ")
    total = int(input("quanto dinheiro "))
    total += int(input("quantas moedas "))
    total += int(input("quantas notas "))
    total += int(input("quantas centavos "))
    return total


def sucesso_transacao(dinheiro_recebido, custo_bebida):
    """ Retorna verdadeiro quando o pagamento for aceito,
     ou falso se o dinheiro for insuficiente."""
    if dinheiro_recebido >= custo_bebida:
        mudanca = round(dinheiro_recebido - custo_bebida, 2)
        print(f"Aqui está {mudanca}, no valor recebido .")
        global custo
        custo += custo_bebida
        return True
    else:
        print("Desculpe, pagamento insuficiente. Por favor, insira mais dinheiro.")
        return False


def fazer_cafe(nome_bebida, pedido_ingredientes):
    """Deduza os ingredientes pedidos para o recurso"""
    for item in pedido_ingredientes:
        recursos[item] -= pedido_ingredientes[item]
    print(f"Aqui esta o seu {nome_bebida}☕ ")


is_on = True

while is_on:
    escolha = input("O QUE VOCÊ DESEJA BEBER? (ESPRESSO/CAFE/CAPPUCINO) : ").lower()
    if escolha == "off":
        break
    elif escolha == "report":
        print(f"Água: {recursos['agua']}ml")
        print(f"Leite: {recursos['leite']}ml")
        print(f"Café: {recursos['cafe']}g")
        print(f"Dinheiro total arrecadado: R${custo}")
    else:
        bebida = MENU.get(escolha)
        if bebida:
            if recursos_suficientes(bebida["ingredientes"]):
                pagamento = processar_pagamento()
                if sucesso_transacao(pagamento, bebida["custo"]):
                    fazer_cafe(escolha, bebida["ingredientes"])