import os
os.system("cls")

while True:
    print("\n--- CALCULADORA --")
    print("1 - Somar")
    print("2 - Subitrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = input("Opção: ")

    match opcao:
        case "1" | "2" | "3" | "4" :
            num1 = float(input("Primeiro Número: "))
            num2 = float(input("Segundo Número: "))

            match opcao:
                case "1":
                    print(f"Resultado: {num1 + num2}")
                case "2":
                    print(f"Resultado {num1 - num2}")
                case "3":
                    print(f"Resultado: {num1 * num2}")
                case "4":
                    if num2 == 0:
                        print("Erro: divisão por zerro não é permitida.")
                    else:
                        print(f"Resultado: {num1 / num2}")
        case "5":
            print("Encerrando a Calculadora...")
            break
        case _:
            print("Opção inválida! Escolha uma outra opção")