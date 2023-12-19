numero = float(input("Digite um número: "))

if numero > 0:
    raiz_quadrada = numero ** 0.5
    print("A raiz quadrada do número {} é: {:.2f}".format(numero,raiz_quadrada))
else:
    print("Número inválido. O número {} é negativo.".format(numero))
