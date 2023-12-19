palavras = ("anime", "genshim Impact", "baldurs gate", "crepusculo", "popmundo")

for palavra in palavras:
    vogais = [letra for letra in palavra if letra in "aeiou"]
    print("{}: {}".format(palavra,vogais))
