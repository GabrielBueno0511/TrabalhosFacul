
# Exercício 9 – Faça um programa que leia três número e mostre estes em ordem decrescente.

n1 = float(input("digite um valor: "))
n2 = float(input("digite um valor: "))
n3 = float(input("digite um valor: "))

if n1 <= n2 and n2 <= n3:
    print(f"A ordem decrescente é: {n3}, {n2} e {n1}")

elif n3 <= n2 and n2 <= n1:
   print(f"A ordem decrescente é: {n1}, {n2} e {n3}")

elif n2 <= n3 and n3 <= n1:
    print(f"A ordem decrescente é: {n1}, {n3} e {n2}")

elif n1 <= n3 and n3 <= n2:
    print(f"A ordem decrescente é: {n2}, {n3} e {n1}")

elif n3 <= n1 and n1 <= n2:
    print(f"A ordem decrescente é: {n2}, {n1} e {n3}")

elif n2 <= n1 and n1 <= n3:
    print(f"A ordem decrescente é: {n3}, {n1} e {n2}")

elif n1 == n2 and n2 == n3:
    print("Todos valores são iguais")

else:
    print("desculpe, por va favor tente novamente")

