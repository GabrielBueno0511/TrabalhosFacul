 # Exercício 1 – Vamos criar um calculadora em Python, você deve pedir que o usuário informe a operação (+, -, *, /) que deseja realizar e dois valores, baseado na operação informada e nos valores, apresente o resultado em tela. Fique a vontade para fazer as validações de valores que julgar necessárias (você irá aplicada: input, print, operações aritméticas básicas e comandos de controle)

v1 = float(input("valor a ser calculado: "))
op = input("qual operação deseja realizar: ")
v2 = float(input("segundo valor do calculo: "))

if op == ("+"):
    print("A soma dos valores tem o resultado: ", v1 + v2)
elif op == ("-"):
    print("A subtração dos valores tem o resultado: ", v1 - v2)
elif op == ("/"):
    print("A divisão dos valores tem o resultado: ", v1 / v2)
elif op == ("*"):
    print("a multiplicação dos valores tem o resultado: ", v1 * v2)
else:
    print("Operação Não identificada")