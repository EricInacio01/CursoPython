print("Digite seu peso abaixo:")
peso = float(input().replace(',', '.'))

print("Digite sua altura abaixo:")
altura = float(input().replace(',', '.'))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Peso ideal, parabéns.")
elif 25.0 <= imc <= 29.9:
    print("Levemente acima do peso")
elif 30.0 <= imc <= 34.9:
    print("Obesidade Grau I")
elif 35.0 <= imc <= 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade III (Mórbida)")
