
#  Exercício 3 – Crie um algoritmo em Python que peça dois valores com casas decimais (float), mostre o resultado da divisão, da multiplicação, do resto (ou módulo) e da divisão inteira

v1 = float(input("digite um valor com casas decimais "))
v2 = float(input("digite outro valor com casas decimais "))

divisao = v1 / v2
multiplicacao = v1 * v2
resto = v1 % v2
divInt = v1 // v2

print(f"divisão = {divisao:.2f}")
print(f"multiplição = {multiplicacao:.2f}")
print(f"resto = {resto}")
print(f" divisão inteira = {divInt}")