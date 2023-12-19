idades = [int(input(f"Digite a idade da {i+1}ª pessoa: ")) for i in range(4)]

media_das_idades = sum(idades) / len(idades)
print("A média das idades é {}.".format(media_das_idades))
