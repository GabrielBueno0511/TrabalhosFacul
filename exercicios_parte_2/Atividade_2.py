# 2. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa em Python que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.


# input de valroes

list_temp=[]

while True:
    temp = float(input("Insira a temperatura: "))
    print(" ")
    cont = input("Deseja continuar inserindo temperaturaa?(\033[32ms\033[m/\033[31mn\033[m)")
    list_temp.append(temp)
    print("-"*50)
    print(" ")
    print(" ")

    if cont == "n":
        break
    if cont == "s":
        (" ")
    
    else:
        print("\033[31mError, invalid input\033[m")
        print(" ")
        break

print(f"A maior temperatura é: {max(list_temp)}°")
print(" ")
print(f"A menor temperatura é: {min(list_temp)}°")
print(" ")

media = sum(list_temp) / len(list_temp)

print(f"A temperatura média: {media}°")