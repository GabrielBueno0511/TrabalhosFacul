# Exercício 8 – Faça um programa que leia três número e mostre o menor e o maior deles.

n1 = float(input("digite um valor: "))
n2 = float(input("digite um valor: "))
n3 = float(input("digite um valor: "))

if n1 <= n2 and n2 <= n3:
    print(f"O maior numero é {n3}, e o menor {n1}")

elif n3 <= n2 and n2 <= n1:
    print(f"O maior numero é {n1}, e o menor {n3}")

elif n2 <= n3 and n3 <= n1:
    print(f"O maior numero é {n1}, e o menor {n2}")

elif n1 <= n3 and n3 <= n2:
    print(f"O maior numero é {n2}, e o menor {n1}")

elif n3 <= n1 and n1 <= n2:
    print(f"O maior numero é {n2}, e o menor {n3}")

elif n2 <= n1 and n1 <= n3:
    print(f"O maior numero é {n3}, e o menor {n2}")

elif n1 == n2 and n2 == n3:
    print("Todos valores são iguais")

else:
    print("desculpe, por favor tente novamente")