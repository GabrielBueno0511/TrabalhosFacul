# Exercício 5 – Crie um algoritmo em Python que peça um valor ao usuário e informe se é dezena, centena ou milhar.

vl = int(input("qualquer valor, e direi se ele é uma centena, dezena ou milhar "))

if vl < 100:
    print(f"O valor {vl} é uma Dezena")


elif vl < 1000:
    print(f"O valor {vl} é uma centena")
    
elif vl < 1000000:
    print(f"O valor {vl} é um milhar")

else:
    print("por favor digite um valor que estre essas casas decimais")