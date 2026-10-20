import os
os.system("cls")

senha = "1234"
tentativas = 3
acesso_concedido = False

while tentativas > 0 and not acesso_concedido:
    senha_digitada = input("Digite a Senha: ")

    if senha_digitada == senha:
        print("Acesso Liberado!")
        acesso_concedido - True
        break
        
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Senha incorreta! Tentativas restante: {tentativas}")
        else:
            print("Acesso Bloqueado. Número de tentativas excedido.")  

