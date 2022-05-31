# Exercício 5 – Um mercadinho de bairro expandiu seus caixas e funcionários, agora eles precisam de um programa que implemente uma caixa registradora simples. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
# Mercadinho BigBom
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
venda = 1
while True:
    print(" ")
    print("Mercadinho BigBom")
    print("-"*50)
    print(f"Venda {venda}")
    venda =  venda + 1

    list = []
    p = 1
    v = 1
    i = 1

    while ( v > 0 ):
        
        v = float(input(f"Produto {i}: por favor insira o valor: R$" ))
        list.append(v)
        i = i + 1
    print("-"*50)

    for valor in list:
        print(f"Produto {p}: R${valor}")
        p = p + 1
    print("-"*50)
    s =  sum(list)
    print(f"Total: R${s} ")
    D = float(input(" Dinheiro: R$"))
    print(" ")
    print(f"Dinheiro: R${D}")

    if D >= s:
        print("Troco: R$", D - s )
    else:
        print("O valor não cobre o valor dos produtos")
        print("encerraremos a compra e iniciaremos outra.")
    print("-"*50)
    print(" ")



