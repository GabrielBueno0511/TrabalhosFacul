# 3. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre  um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa  no crime. Se a pessoa responder positivamente a 2 questões ela deve ser  classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".
list=[]
#perguntas
print("Responda as perguntar somente com sim ou não")
print("Se não responder sim ou não sera considerado como sim")

#perguntas A
pgt_a = input("Telefonou para a vítima?")


if pgt_a == "sim":
   pgt_a = 1
   list.append(pgt_a)

elif pgt_a == "não":
    pgt_a = 0
    list.append(pgt_a)

else:
    print("Resposta não objetiva")
    pgt_a = 1
    list.append(pgt_a)

print(" ")
print("-"*50)      


#perguntas B
pgt_b = input("Esteve no local do crime?")



if pgt_b == "sim":
   pgt_b = 1
   list.append(pgt_b)

elif pgt_b == "não":
    pgt_b = 0
    list.append(pgt_b)

else:
    print("Resposta não objetiva")
    pgt_a = 1
    list.append(pgt_a) 



print(" ")
print("-"*50)



#perguntas C
pgt_c = input("Mora perto da vítima?")



if pgt_c == "sim":
   pgt_c = 1
   list.append(pgt_c)

elif pgt_c == "não":
    pgt_c = 0
    list.append(pgt_c)

else:
    print("Resposta não objetiva")
    pgt_c = 1
    list.append(pgt_c)  

print(" ")
print("-"*50)

#perguntas D
pgt_d = input("Devia para a vítima?")


if pgt_d == "sim":
   pgt_d = 1
   list.append(pgt_d)

elif pgt_d == "não":
    pgt_d = 0
    list.append(pgt_d)

else:
    print("Resposta não objetiva")
    pgt_d = 1
    list.append(pgt_d) 

print(" ")
print("-"*50)


#perguntas E
pgt_e = input("Já trabalhou com a vítima?")



if pgt_e == "sim":
   pgt_e = 1
   list.append(pgt_e)

elif pgt_e == "não":
    pgt_e = 0
    list.append(pgt_e)

else:
    print("Resposta não objetiva")
    pgt_e = 1
    list.append(pgt_e)  

print(" ")
print("-"*50)

# classificação
print("-"*50)

nivel_suspeita = sum(list)

if nivel_suspeita == 5:
    print("Classificação : \033[31mAssassino\033[m")

elif nivel_suspeita == 2:
    print("Classificado : \033[35mSuspeito\033[m")

elif nivel_suspeita >= 3:
    print("classificado : \033[33mCúmplice\033[m")

else:
    print("Classificado : \033[32mInocente\033[m")

print("-"*50)
    











