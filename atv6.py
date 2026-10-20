while True:
    numeroTabuada = int(input("Digite um número para ver a tabuada: "))
    limiteTabuada = int(input("Digite o limite da tabuada: "))
    if limiteTabuada < 1 or limiteTabuada > 20:
        print("O limite da tabuada deve estar entre 1 e 20. Por favor, digite um limite válido.")
    else:
        limiteTemp = 1
        while limiteTemp < limiteTabuada + 1:
            resultado = numeroTabuada * limiteTemp
            print(f"{numeroTabuada} x {limiteTemp} = {resultado}")
            limiteTemp += 1
    opcao = input("Deseja ver outra tabuada? (s/n): ")

    while opcao != 'S' and opcao != 's' and opcao != 'n' and opcao != 'N':
        opcao = input("ERRO! Digite S ou N: ")

    if opcao == 'n' or opcao == 'N':
        break
print("Programa encerrado.")
