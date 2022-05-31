#  Exercício 10 – Faça um algoritmo que peça um horário e informe o período do dia, matutino,vespertino ou noturno.

hora = float(input("diga um horarios(para determinar o horario e minutos ude ponto por favor): "))

if hora >= 0 and hora <= 5.59:
    print(f"{hora} é no periodo matutino")

elif hora >= 6 and hora <= 11.59:
    print(f"{hora} é no periodo vespetino")

elif hora >= 12 and hora <= 17.59:
    print(f"{hora} é no periodo dia")

elif hora >= 18 and hora <= 23.59:
    print(f"{hora} é no periodo noturno")

else:    
    ("por favos ensira um horario entre 0 e 24.59 horas")