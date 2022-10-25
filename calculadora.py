print("=" * 198)

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite sua peso: "))
imc = peso/altura**2

print("=" * 198)

print("Os dados coletados foram: ")
print("Seu nome", nome)
print("Seu idade", idade, "anos")
print("Sua altura", altura, "m")
print("Seu peso", peso, "Kg")
print("IMC = ", imc)

print("=" * 198)
