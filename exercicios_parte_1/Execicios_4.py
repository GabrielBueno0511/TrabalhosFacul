# Exercício 4 – Faça um algoritmo em Python que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5! = 5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo: 
# Fatorial de 5: 5! = 5 * 4 * 3 * 2 * 1 = 120


n = int(input("insira um valor: "))
i = n+1
Fat = 1

print(f"{n}! = ", end="")
while(i > 1):
    i = i - 1
    print( i, end="")
    print( " X " if i > 1 else " = ", end="")
    Fat = Fat * i
print(Fat)

    


