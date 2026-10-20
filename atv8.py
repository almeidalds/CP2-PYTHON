soma = 0
positivos = 0
negativos = 0
pares = 0
impares = 0
numerosDigitados = 0

while True:
    numeroDigitado = int(input("Digite um número (ou '0' para encerrar): "))
    if numeroDigitado == 0:
        break
    numerosDigitados += 1
    if numerosDigitados == 1 :
        maiorNumero = numeroDigitado
        menorNumero = numeroDigitado
    else:
        if numeroDigitado > maiorNumero:
            maiorNumero = numeroDigitado
        if numeroDigitado < menorNumero:
            menorNumero = numeroDigitado

    soma += numeroDigitado

    if numeroDigitado > 0:
        positivos += 1
    elif numeroDigitado < 0:
        negativos += 1

    if numeroDigitado % 2 == 0:
        pares += 1
    elif numeroDigitado % 2 != 0:
        impares += 1

if numerosDigitados == 0:
    print("Nenhum número foi digitado.")
else:
    print(f"\n\nPositivo: {positivos}\nNegativo: {negativos}\nPares: {pares}\nÍmpares: {impares}\nSoma: {soma}\nMaior número digitado: {maiorNumero}\nMenor número digitado: {menorNumero}")
