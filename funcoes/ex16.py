def calcular_multa(velocidade, limite):
    if velocidade > limite:
        diferenca = velocidade - limite
        multa = diferenca * 7 
        return multa
    else:
        return 0  

limite_velocidade = 42
velocidade_carro = int(input("Digite a velocidade do carro (em km/h): "))

valor_multa = calcular_multa(velocidade_carro, limite_velocidade)

if valor_multa > 0:
    print("Calma lá, cidadão! Você ultrapassou o limite de velocidade estipulado. A multa é de R${:.2f}. Bora passear no patio?".format(valor_multa))
else:
    print("Você está dentro dos parametros da lei, tenha um bom dia!.")
