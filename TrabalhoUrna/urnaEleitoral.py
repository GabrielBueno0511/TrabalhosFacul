
# O Brasil tem um grava problema quando falamos em política, porém podemos ter ações que podem melhorar alguns dos fatores. A primeira que teremos é criar um algoritmo base para a Urna Eletrônica. Nesse algoritmo teremos apenas 5 canditados por enquanto:
# 1 - Vincent Vega
# 2 - Rick Dalton
# 3 - Shoshanna Dreyfus
# 4 - Beatrixx Kido
# 5 - Jules Winnfield
# Vocês devem criar um algoritmo que pergunte quantos eleitores irão participar, cada eleitos terá direito a apenas um foto, porém se realizar um voto errado (um número de candidato que não existe), tem 5 chances até informar um voto válido. No final deve informar a porcentagem de votos de todos os candidatos e quem foi eleito. Não precisa considerar segundo turno. Caso ocorra um empate, mostrar quais os nomes empatados e porcentagem de empate.

# Obs: o desafio é não usar listas na implementação


numero_eleitores = int(input("Numero de eleitores: "))

print("Esses são os respectivos candidatos: ")
print("1 - Vincent Vega")
print ("2 - Rick Dalton")
print("3 - Shoshanna Dreyfus")
print("4 - Beatrixx Kido")
print("5 - Jules Winnfield")

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
candidato_5 = 0


eleitor = 1

for cand in range(numero_eleitores):
    print(" ")
    print("-------------------------------------------------------------------------------")
    print(f"Eleitor {eleitor}")
    eleitor = eleitor + 1
    print("por favor vote através do numero que representa o seu candidato!!")
    voto = input("Nome do candidato: ")
    if voto == "1":
        candidato_1 = candidato_1 + 1
        print("você votou em Vincent Vega!")
    
    elif voto == "2":
         candidato_2 = candidato_2 + 1
         print("você votou em Rick Dalton!")

    elif voto == "3":
         candidato_3 = candidato_3 + 1
         print("você votou em Shoshanna Dreyfus!")

    elif voto == "4":
         candidato_4 = candidato_4 + 1
         print("você votou em Beatrixx Kido!")

    elif voto == "5":
         candidato_5 = candidato_5 + 1
         print("você votou em Jules WinnfieldS!")
    
    else:
        print("esse numero não corresponde a nenhum candidato, tente novamente")
        print("Esses são os respectivos candidatos: ")
        print("1 - Vincent Vega")
        print ("2 - Rick Dalton")
        print("3 - Shoshanna Dreyfus")
        print("4 - Beatrixx Kido")
        print("5 - Jules Winnfield")

        c = 2

        while True:
            
            print("por favor, vote através do numero que representa o seu candidato!!")
            voto = input("Numero do candidato: ")
            if voto == "1":
                candidato_1 = candidato_1 + 1
                break
        
            elif voto == "2":
                candidato_2 = candidato_2 + 1
                break

            elif voto == "3":
                candidato_3 = candidato_3 + 1
                break

            elif voto == "4":
                candidato_4 = candidato_4 + 1
                break

            elif voto == "5":
                candidato_5 = candidato_5 + 1
                break
            
            else:
                print(f"você tentou {c} vezes, seu limite são 5 chances")
                c = c + 1
                if c == 6:
                    break

print("------------------------------------------------------------------------------")
print(" ")

print("Os candidados tiveram a quantidade de votos a seguir: ")

soma = (candidato_1 + candidato_2 + candidato_3 + candidato_4 + candidato_5)

porcentagem_por_voto = 100 / soma

por_cand_1 = porcentagem_por_voto * candidato_1
por_cand_2 = porcentagem_por_voto * candidato_2
por_cand_3 = porcentagem_por_voto * candidato_3
por_cand_4 = porcentagem_por_voto * candidato_4
por_cand_5 = porcentagem_por_voto * candidato_5

print(f"1 - Vincent Vega = {candidato_1} votos, representa {por_cand_1 :.2f} % dos votos")
print (f"2 - Rick Dalton = {candidato_2} votos, representa {por_cand_2 :.2f} % dos votos")
print(f"3 - Shoshanna Dreyfus = {candidato_3} votos, representa {por_cand_3 :.2f} % dos votos")
print(f"4 - Beatrixx Kido = {candidato_4} votos, representa {por_cand_4 :.2f} % dos votos")
print(f"5 - Jules Winnfield = {candidato_5} votos, representa {por_cand_5 :.2f} % dos votos")

print("-------------------------------------------------------------------------------")
print(" ")

if candidato_1 > candidato_2 and candidato_1 > candidato_3 and candidato_1 > candidato_4 and candidato_1 > candidato_5:
    print(f" Vincent Vega foi o vencedor!! com {por_cand_1 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_1 == candidato_2 and candidato_1 > candidato_3 and candidato_1 > candidato_4 and candidato_1 > candidato_5:
    print(f" Vincent Vega e Rick Dalton empataram!! com {por_cand_1 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_1 == candidato_2 and candidato_1 == candidato_3 and candidato_1 > candidato_4 and candidato_1 > candidato_5:
    print(f" Vincent Vega, Rick Dalton e Shoshanna Dreyfus empataram!! com {por_cand_1 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_1 == candidato_2 and candidato_1 == candidato_3 and candidato_1 == candidato_4 and candidato_1 > candidato_5:
    print(f" Vincent Vega, Rick Dalton, Shoshanna Dreyfus e Beatrixx Kido empataram!! com {por_cand_1 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_1 == candidato_2 and candidato_1 == candidato_3 and candidato_1 == candidato_4 and candidato_1 == candidato_5:
    print(f" todos candidatos empataram!! com {por_cand_1 :.2f}% dos votos, PARABÉNS!! ")
    


elif candidato_1 > candidato_2 and candidato_1 == candidato_3 and candidato_1 > candidato_4 and candidato_1 > candidato_5:
    print(f" Vincent Vega e Shoshanna Dreyfus empataram!! com {por_cand_1 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_1 > candidato_2 and candidato_1 > candidato_3 and candidato_1 == candidato_4 and candidato_1 > candidato_5:
    print(f" Vincent Vega e Beatrixx Kido empataram!! com {por_cand_1 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_1 > candidato_2 and candidato_1 > candidato_3 and candidato_1 > candidato_4 and candidato_1 == candidato_5:
    print(f" Vincent Vega e Jules Winnfield empataram!! com {por_cand_1 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_2 > candidato_1 and candidato_2 > candidato_3 and candidato_2 > candidato_4 and candidato_2 > candidato_5:
    print(f" Rick Dalton foi o vencedor!! com {por_cand_2 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_2 > candidato_1 and candidato_2 == candidato_3 and candidato_2 > candidato_4 and candidato_2 > candidato_5:
    print(f" Rick Dalton e Shoshanna Dreyfus empataram!! com {por_cand_2 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_2 > candidato_1 and candidato_2 > candidato_3 and candidato_2 == candidato_4 and candidato_2 > candidato_5:
    print(f" Rick Dalton e Beatrixx Kido empataram!! com {por_cand_2 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_2 > candidato_1 and candidato_2 == candidato_3 and candidato_2 == candidato_4 and candidato_2 > candidato_5:
    print(f" Rick Dalton, Shoshanna Dreyfus e Beatrixx Kido empataram!! com {por_cand_2 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_2 > candidato_1 and candidato_2 == candidato_3 and candidato_2 == candidato_4 and candidato_2 == candidato_5:
    print(f" Rick Dalton, Shoshanna Dreyfus, Beatrixx Kido e Jules Winnfield empataram!! com {por_cand_2 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_3 > candidato_1 and candidato_3 > candidato_2 and candidato_3 > candidato_4 and candidato_3 > candidato_5:
    print(f" Shoshanna Dreyfus foi o vencedor!! com {por_cand_3 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_3 > candidato_1 and candidato_3 > candidato_2 and candidato_3 == candidato_4 and candidato_3 == candidato_5:
    print(f" Shoshanna Dreyfus, Beatrixx Kido e Jules Winnfield foi  empataram!! com {por_cand_3 :.2f}% dos votos, PARABÉNS!! ")


elif candidato_3 > candidato_1 and candidato_3 > candidato_2 and candidato_3 == candidato_4 and candidato_3 > candidato_5:
    print(f" Shoshanna Dreyfus e Beatrixx Kido empataram!! com {por_cand_3 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_4 > candidato_1 and candidato_4 > candidato_2 and candidato_4 > candidato_3 and candidato_4 > candidato_5:
    print(f" Beatrixx Kido foi o vencedor!! com {por_cand_4 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_4 > candidato_1 and candidato_4 > candidato_2 and candidato_4 > candidato_3 and candidato_4 == candidato_5:
    print(f" Beatrixx Kido e Jules Winnfield empataram!! com {por_cand_4 :.2f}% dos votos, PARABÉNS!! ")

elif candidato_5 > candidato_1 and candidato_5 > candidato_2 and candidato_5 > candidato_3 and candidato_5 > candidato_4:
    print(f" Jules Winnfield foi o vencedor!! com {por_cand_5 :.2f}% dos votos, PARABÉNS!! ")


else:
    print("erro de contagem")