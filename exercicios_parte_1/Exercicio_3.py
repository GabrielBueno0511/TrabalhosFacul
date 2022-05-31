# Exercício 2 – Vamos calcular a média do nosso aluno e verificar se o mesmo está aprovado,
# reprovado ou de exame. O usuário deve informar 4 notas, sendo uma nota de prova, uma de
# trabalho, uma de atividades e outro de participação. A nota da prova tem peso 4, a nota de
# trabalho tem peso 3, a nota de atividades tem peso 2 e a nota de participação tem peso 1.
# Calcule a média pondera e partir dessa média informe qual a situação acadêmica do aluno.
# Exercício 3 – Você foi contratado por um grande indústria da sua cidade para auxiliar o RH com
# o desenvolvimento de um software, a empresa foi comprada por um grande grupo
# internacional, isso foi uma boa notícia para todos os funcionários pois irão receber um aumento.
# O seu papel como desenvolvedor é criar um programa que irá ajudar o RH a calcular os reajustes.
# Para desenvolver você precisa saber de algumas regras, todos os funcionários irão receber
# algum aumento, mas essa porcentagem vai variar conforme as faixas salariais da seguinte forma:
# • salários até R$ 800,00 : aumento de 20%
# • salários acima de R$ 800,00 até R$ 1300,00 : aumento de 15%
# • salários acima de R$ 1300,00 e R$ 2500,00 : aumento de 10%
# • salários de R$ 2500,00 em diante: aumento de 5%
# Após o aumento ser realizado, informe na tela:
# • o salário antes do reajuste;
# • o percentual de aumento aplicado;
# • o valor do aumento;
# • o novo salário, após o aumento.

Sa = float(input("valor do salário para o reajuste: "))

# salários até R$ 800,00 :

if Sa <= 800:
     V = Sa * 1.20
     print(F"O valor do salário antes do reajuste era de {Sa:.2f} R$")
     print(f"valor após o reajuste é de: {V}")
     print("O valor de reajuste aplicado foi de 20%")
     Va = ( V - Sa)
     print(f"O valor do agregado para o reajuste foi de {Va:.2f} R$")

#  • salários acima de R$ 800,00 até R$ 1300,00 : aumento de 15%

elif Sa > 800 and Sa < 1300:
     V = Sa * 1.15
     print(F"O valor do salário antes do reajuste era de {Sa:.2f} R$")
     print(f"valor após o reajuste é de: {V}")
     print("O valor de reajuste aplicado foi de 15%")
     Va = ( V - Sa)
     print(f"O valor do agregado para o reajuste foi de {Va:.2f} R$")


# • salários acima de R$ 1300,00 e R$ 2500,00 : aumento de 10%

elif Sa > 1300 and Sa < 2500:
     V = Sa * 1.10
     print(F"O valor do salário antes do reajuste era de {Sa:.2f} R$")
     print(f"valor após o reajuste é de: {V}")
     print("O valor de reajuste aplicado foi de 10%")
     Va = ( V - Sa)
     print(f"O valor do agregado para o reajuste foi de {Va:.2f} R$")

# • salários de R$ 2500,00 em diante: aumento de 5%

else:
     V = Sa * 1.05
     print(F"O valor do salário antes do reajuste era de {Sa:.2f} R$")
     print(f"valor após don reajuste é de: {V}")
     print("O valor de reajuste aplicado foi de 05%")
     Va = ( V - Sa)
     print(f"O valor do agregado para o reajuste foi de {Va:.2f} R$")


