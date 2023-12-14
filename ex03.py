temperatura = int(input("qual temperatura? "))

if temperatura <= 20 : {
    print ("está fazendo {} graus lá fora, portanto, está frio".format(temperatura))
}
elif temperatura >= 30 : {
    print ("está fazendo {} graus lá fora, portanto, está quente".format(temperatura))
}
else: {
    print ("está fazendo {} graus lá fora, portanto, está agradavel".format(temperatura))
}