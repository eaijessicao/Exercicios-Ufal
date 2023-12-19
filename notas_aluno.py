nota1 =  float(input("Quanto você tirou na primeira prova?"))
nota2 =  float(input("Quanto você tirou na segunda prova?"))

media = (nota1 + nota2) / 2

if media >= 5: {
    print("Parabens, a sua media foi de {}, logo, você está aprovado".format(media))
}

else : {
    print("A sua media foi de {}, boa sorte na proxima!".format(media))
}