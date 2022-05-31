# Exercício 2 – Vamos calcular a média do nosso aluno e verificar se o mesmo está aprovado, reprovado ou de exame. O usuário deve informar 4 notas, sendo uma nota de prova, uma detrabalho, uma de atividades e outro de participação. A nota da prova tem peso 4, a nota de trabalho tem peso 3, a nota de atividades tem peso 2 e a nota de participação tem peso 1. Calcule a média pondera e partir dessa média informe qual a situação acadêmica do aluno.
print(" A seguir insira as notas do aluno:")

N1 = float(input("nota da prova: "))
NoPr = N1 * (4 / 10)

N2 = float(input("nota do trabalho: "))
NoTr = N2 * (3 / 10)

N3 = float(input("nota das atividades: "))
NoAt = N3 * (2 / 10)

N4 = float(input("nota de participação: "))
NoPa = N4 * (1 / 10)

media = (NoAt + NoPa + NoTr + NoPr)

if media >= 8:
    print(f"A media do aluno é: {media}")
    print("O aluno esta aprovado!")
elif media >= 5:
    print(f"A nota do aluno é: {media} ")
    print("O aluno esta de exame.")
else:
    print(f"A nota do aluno é: {media} ")
    print("O aluno esta reprovado")

