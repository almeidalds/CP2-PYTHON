saldo = 500
while True:
    print("\n\nBem-vindo ao sistema bancário! \n \n"
          "Para consultar o saldo, digite 'saldo'; \n"
          "Para realizar um depósito, digite 'deposito'; \n"
          "Para realizar um saque, digite 'saque'; \n"
          "Para sair, digite 'sair'. ")

    operacao = input("Digite a operação desejada: ")

    match operacao:
        case "saldo" | "Saldo" | "sáldo" | "Sáldo" | "SALDO":
            print("\nO saldo atual da conta é: R$", saldo)
        case "deposito" | "Deposito" | "depósito" | "Depósito" | "DEPOSITO" | "DEPÓSITO" | "depositar" | "Depositar" | "DEPOSITAR":
            valorDeposito = float(input("Digite o valor do depósito: R$"))
            if valorDeposito <= 0:
                print("\nValor inválido. O depósito deve ser maior que zero.")
            else:
                saldo += valorDeposito
                print("\nDepósito realizado com sucesso! Novo saldo: R$", saldo)
        case "saque" | "Saque" | "sáque" | "Sáque" | "SAQUE" | "SÁQUE" | "sacar" | "Sacar" | "SACAR":
            valorSaque = float(input("Digite o valor do saque: R$"))
            if valorSaque <= 0:
                print("\nValor inválido. O saque deve ser maior que zero.")
            elif valorSaque > saldo:
                print("\nSaldo insuficiente para realizar o saque.")
            else:
                saldo -= valorSaque
                print("\nSaque realizado com sucesso! Novo saldo: R$", saldo)
        case "sair" | "Sair" | "SAIR":
            print("\nSaindo do sistema bancário. Até logo!")
            break
        case _:
            print("\nOperação inválida. Por favor, escolha uma operação válida.")
