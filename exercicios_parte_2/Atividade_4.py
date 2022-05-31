# 4. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
# O resultado do atleta será determinado pela média dos cinco valores restantes. 
# Você deve fazer um programa em Python utilizando listas, que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o  nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o 
# exemplo abaixo:
# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

while True:
    nome_atleta = input("Nome do atleta: ")
    if nome_atleta == "":

        print(" ")
        print("-"*50)
        print(" ")

        print("\033[31mprograma finalizado\033[m")

        print(" ")
        print("-"*50)
        print(" ")

    
        break

    else:
    

# input de saltos

        i = 1
        list_saltos = []

        while i < 6:

            salto = float(input(f"{i}° Salto: "))
            i +=1
            list_saltos.append(salto)
        print(" ")
        print("-"*50)
        print(" ")




# print final

        print(f"Nome do Atleta: {nome_atleta}")
        print(f"saltos: {list_saltos[0]}m - {list_saltos[1]}m - {list_saltos[2]}m - {list_saltos[3]}m - {list_saltos[4]}m")
        media = sum(list_saltos) / len(list_saltos)
        print(f"média dos saltos: {media}")
        print(" ")
        print("#"*50)
        print(" ")

