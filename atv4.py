import os
os.system("cls")

num_secreto = 13
max_tentativas = 7
tentativas_atual = 1
acertou = False

while tentativas_atual <= max_tentativas and not acertou:
    palpite = int(input(f"Tentativa {tentativas_atual}/{max_tentativas} - Digite seu palpite: "))

    if palpite ==  num_secreto:
        print(f"{palpite}: acertou em {tentativas_atual} tentativas!")
        acertou = True

    elif palpite < num_secreto:
        print(f"{palpite}: tente um número maior.")
        tentativas_atual += 1
    else:
        print(f"{palpite}: tente ym número menor.")
        tentativas_atual +=1

if not acertou:
    print(f"Sua tentativas acabaram! O número secreto era: {num_secreto}")