totalVeiculos = 0
totalArrecadado = 0

while True:
    placa = input("Digite a placa do veículo: ").upper()
    if placa == "FIM":
        break
    horas = int(input("Digite a quantidade de horas que o veículo ficou estacionado: "))
    if horas <= 0:
        print("Quantidade de horas inválida. Por favor, digite um número maior que zero.")
        continue
    if horas > 8:
        multa = 20
    else:
        multa = 0
    totalVeiculos += 1
    calculoValor = 8 + (horas - 1) * 5 + int(multa)
    totalArrecadado += calculoValor
    print(f"Placa: {placa} : R$ {calculoValor}")

print(f"\n\nTotal de veículos: {totalVeiculos}")
print(f"\nTotal arrecadado: R$ {totalArrecadado}")
