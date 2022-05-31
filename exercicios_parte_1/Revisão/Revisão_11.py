# Em Python, vamos fazer um tabuada, seu objetivo é desenvolver um algoritmo que a partir de uma número informado pelo usuário você mostra a tabuada de 1 a 10 dessa valor.

N1 = float(input("De um numero para seus produtos, sendo multiplicados de 1 a 10"))

i = 0

while (i <= 10 ):
    print(f"{N1} x {i} =", N1 * i)
    i = i + 1