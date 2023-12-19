pessoas_com_maioridade = 0
homens_cadastro = 0
mulheres_menor_de_20 = 0

while True:
    idade = int(input("Qual é a sua idade? : "))
    sexo = input("Digite M ou F para definir o genêro: ")

    if idade > 18:
        pessoas_com_maioridade += 1
    if sexo == 'm':
        homens_cadastro += 1
    elif sexo == 'f' and idade < 20:
        mulheres_menor_de_20 += 1

    if input("Deseja cadastrar mais uma pessoa? (S/N): ").upper() != 'S':
        print("você encerrou o cadastro")

        break

print("A quantidade de pessoas maiores de 18 anos é:  {}".format(pessoas_com_maioridade))
print("Quantidade de homens cadastrados é de: {} homens".format(homens_cadastro))
print("Quantidade de mulheres com menos de 20 anos é de : {} mulheres".format(mulheres_menor_de_20))
