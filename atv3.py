import os
os.system("cls")

total_notas = 0
soma_notas = 0.0

while True:
    nota = float(input("Digite uma nota(-1 para encerrar): "))

    if nota == -1:
        break

    if 0 <= nota <= 10:
        soma_notas += nota
        total_notas += 1
    else:
        print("Nota inválida Digite apenas valores entre 0 e 10")

if total_notas == 0:
    print("Nenhuma nota Válida foi digitada.")
else:
    media = soma_notas / total_notas

    if media < 5.0:
        clasificacao = "insuficiente"
    elif media < 7.0:
        clasificacao = "Regular"
    elif media < 9.0:
        clasificacao = "Boa"
    else:
        clasificacao = "Excelente"

    print(f"Quantidade de Notas: {total_notas}")
    print(f"Média da Turma: {media:.2f}")
    print(f"Classificação: {clasificacao}")