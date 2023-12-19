valor_saque = int(input("O saque vai ser de quanto hoje? Digite em R$: "))

notas_de_50 = valor_saque // 50
resto = valor_saque % 50
notas_de_20 = resto // 20
resto %= 20
notas_de_10 = resto // 10
moedas_de_1 = resto % 10

mensagem_do_caixa = "Olá, meu patrão! Você sacou R${}. Serão fornecidas {} notas de R$50, {} notas de R$20, {} notas de R$10 e {} moedas de R$1.".format(valor_saque, notas_de_50, notas_de_20, notas_de_10, moedas_de_1)

print(mensagem_do_caixa)
