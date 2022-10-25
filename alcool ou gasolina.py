print("=" * 198)
Gasolina= float(input("Preço do litro da Gasolina:"))
Alcool = float(input("Preço do litro Alcool: "))
print("=" * 198)

a = Alcool/Gasolina

if a <= 0.7:
    print("Gasolina")
else:
    print("Alcool")
print("=" * 198)