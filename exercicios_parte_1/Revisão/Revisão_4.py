
# Exercício 4 – Crie um algoritmo em Python que peça um valor inteiro (int) ao usuário e informe qual intervalo de dezena ele se encaixa. Por exemplo: valor 9 a dezena é 0, valor 16 a dezena é 1, valor 62 a dezena é 6. Existe de mais uma forma de resolver com lógica bem diferentes.

valor = int(input("digite um numero de 0 a 100 para saber qual e sua dezena: "))

dezena = valor // 10

print(f"A dezena desse nunmero é {dezena}")


