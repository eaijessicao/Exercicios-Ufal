numeros_por_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
                       "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

numero = int(input("Digite um número entre 0 e 20, meu consagrado: "))

if 0 <= numero <= 20:
    print(numeros_por_extenso[numero])
else:
    print("O número não está dentro da extensão estipulada, tem certeza que digitou um numero entre 0 a 20?")
