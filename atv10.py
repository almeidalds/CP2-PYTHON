nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))
quantidadeEstoque = int(input("Digite a quantidade em estoque: "))
totalVendido = 0
while True:
    print("\n\nBem-vindo ao sistema de gerenciamento de estoque! \n \n"
          "Para consultar o estoque do produto, digite 'estoque'; \n"
          "Para repor o estoque, digite 'repor'; \n"
          "Para realizar uma venda, digite 'venda'; \n"
          "Para sair, digite 'sair'. ")

    operacao = input("Digite a operação desejada: ")

    match operacao:
        case "estoque" | "Estoque" | "ESTOQUE":
            print(f"\nO estoque do produto {nome} é: {quantidadeEstoque}")
        case "repor" | "Repor" | "REPOR":
            quantidadeRepor = int(input("Digite a quantidade a ser reposta: "))
            if quantidadeRepor <= 0:
                print("\nQuantidade inválida. A quantidade a ser reposta deve ser maior que zero.")
            else:
                quantidadeEstoque += quantidadeRepor
                print(f"\nEstoque reposto com sucesso! Novo estoque: {quantidadeEstoque}")
        case "venda" | "Venda" | "VENDA":
            quantidadeVenda = int(input("Digite a quantidade a ser vendida: "))
            if quantidadeVenda <= 0:
                print("\nQuantidade inválida. A quantidade a ser vendida deve ser maior que zero.")
            elif quantidadeVenda > quantidadeEstoque:
                print(f"\nQuantidade insuficiente em estoque. O estoque atual é: {quantidadeEstoque}")
            else:
                quantidadeEstoque -= quantidadeVenda
                totalVendido += quantidadeVenda * preco
                print(f"\nVenda realizada com sucesso! Novo estoque: {quantidadeEstoque}")
        case "sair" | "Sair" | "SAIR":
            print("\nSaindo do sistema de gerenciamento de estoque. Até logo!")
            print(f"Estoque restante: {quantidadeEstoque}")
            print(f"Total vendido: R$ {totalVendido}")
            break
        case _:
            print("\nOperação inválida. Por favor, escolha uma operação válida.")
