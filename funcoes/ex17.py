def calcular_salario(salario):
    if salario < 1250:
        aumento = salario * 0.15  
    else:
        aumento = salario * 0.10  
    
    aumento_salario = salario + aumento 
    
    return aumento_salario

salario_inicial = float(input("Digite o seu salario:  "))
aumento_salario = calcular_salario(salario_inicial)

print("Parabens! O seu novo salário é: R${:.2f}.".format(aumento_salario))
