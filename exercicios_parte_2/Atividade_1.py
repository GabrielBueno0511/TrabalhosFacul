# 1. A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa em Python que gere a série até que o valor seja maior que 500.


v1 = 0
v2 = 1
v3 = 1

while True:
    v3 = 0
    v3 = v2 + v1
    v1 = v2
    v2 = v3
        
    print(v1)

    if v1 > 500:
        break