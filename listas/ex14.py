pessoas = []
pessoas_mais_pesadas = []
pessoas_mais_leves = []

quantidade = int(input("Quantas pessoas deseja cadastrar? "))

for _ in range(quantidade):
    nome = input("Digite o nome da pessoa escolhida: ")
    peso = float(input("Digite o peso da pessoa escolhida: "))
    pessoa = (nome, peso)
    pessoas.append(pessoa)
pessoas_mais_pesadas = sorted(pessoas, key=lambda x: x[1], reverse=True)[:3]
pessoas_mais_leves = sorted(pessoas, key=lambda x: x[1])[:3]

print(f"Foram cadastradas cerca de {len(pessoas)} pessoa(s).")
print("top 3 pessoas mais pesadas:", pessoas_mais_pesadas)
print("top 3 pessoas mais leves:", pessoas_mais_leves)
