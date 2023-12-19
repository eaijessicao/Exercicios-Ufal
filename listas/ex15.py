matriz = []

for _ in range(3):
    linha = input("Digite um numero: ").split()
    matriz.append(linha)

for linha in matriz:
    print(" ".join(linha))
