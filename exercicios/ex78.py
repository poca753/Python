jogadores = {}

for i in range(6):
    nome = input(f"Digite o nome do {i+1}º jogador: ")
    resultado = float(input(f"Digite o resultado de {nome}: "))
    jogadores[nome] = resultado

decrescente = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)

crescente = sorted(jogadores.items(), key=lambda item: item[1])

print("\nResultados em ordem decrescente:")
for nome, resultado in decrescente:
    print(f"{nome}: {resultado}")

print("\nResultados em ordem crescente:")
for nome, resultado in crescente:
    print(f"{nome}: {resultado}")
