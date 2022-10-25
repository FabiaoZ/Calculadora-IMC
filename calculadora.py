print("=" * 198)
#declarando variáveis
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite sua peso: "))
imc = peso/altura**2 #fórmula para calcular imc

print("=" * 198)
#saida de dados
print("Os dados coletados foram: ")
print("Seu nome: ", nome)
print("Seu idade: ", idade, "anos")
print("Sua altura: ", altura, "m")
print("Seu peso: ", peso, "Kg")
print("Seu IMC: ", imc)

print("=" * 198)

if imc <= 16:
    print("Magreza grave")
elif imc < 18.5:
    print("Magreza Leve")
elif imc < 24.9:
    print("Saudável")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 34.9:
    print("Obesidade")
elif imc < 39.9:
    print("Obesidade Severa")
else:
    print("Obesidade Mórbida")

print("=" * 198)