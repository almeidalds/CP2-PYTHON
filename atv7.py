numeroDeEleitores = int(input("Digite o número de eleitores: "))
eleitoresQueVotaram = 0
projeto1 = 0
projeto2 = 0
projeto3 = 0
votosNulos = 0
votosBrancos = 0
while numeroDeEleitores <= 0:
    print("Número de eleitores inválido. Por favor, digite um número maior que zero.")
    numeroDeEleitores = int(input("Digite o número de eleitores: "))

while eleitoresQueVotaram < numeroDeEleitores:
    eleitoresQueVotaram += 1
    voto = input("Digite o voto do eleitor: ")
    match voto:
        case "1":
            projeto1 += 1
            print("Voto registrado para o projeto 1.")
        case "2":
            projeto2 += 1
            print("Voto registrado para o projeto 2.")
        case "3":
            projeto3 += 1
            print("Voto registrado para o projeto 3.")
        case "0":
            votosBrancos += 1
            print("Voto branco.")
        case _:
            votosNulos += 1
            print("Voto nulo.")

print("\n\nResultado: \n\nProjeto 1: ", projeto1, " votos. \nProjeto 2: ", projeto2, " votos. \nProjeto 3: ", projeto3, " votos. \nVotos nulos: ", votosNulos, " votos. \nVotos brancos: ", votosBrancos, " votos." )

#Calculando o vencedor

if projeto1 > projeto2 and projeto1 > projeto3:
    vencedor = "Projeto 1"
    print("\n\nO vencedor é: ", vencedor)
elif projeto2 > projeto1 and projeto2 > projeto3:
    vencedor = "Projeto 2"
    print("\n\nO vencedor é: ", vencedor)
elif projeto3 > projeto1 and projeto3 > projeto2:
    vencedor = "Projeto 3"
    print("\n\nO vencedor é: ", vencedor)
else:
    print("\n\nHouve um empate entre os projetos. Nenhum projeto venceu.")
