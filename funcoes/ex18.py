def calcular_status(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(f"A média do aluno é: {media}")
    if media >= 7 and media <= 10:
        return "Parabens! a sua media foi de {}, você está aprovado!".format(media)
    elif media < 7:
        return "Bons estudos, a sua media foi de {}, você ficou de recuperação!".format(media)
    else:
        return "Boa sorte na proxima, a sua media foi de {}, você está reprovado!".format(media)



nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
status = calcular_status(nota1, nota2)
print("Status: {}".format(status))



