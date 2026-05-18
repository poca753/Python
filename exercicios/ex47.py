from random import randint
from time import sleep

# Exibição das opções
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

# Entrada da jogada do jogador
jogada = int(input("Qual é a sua jogada? "))

# Jogada do computador
jogadapc = randint(0, 2)

# Itens correspondentes às jogadas
itens = ("Pedra", "Papel", "Tesoura")

# Animação do jogo
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

# Exibição das escolhas
print("-=" * 10)
print(f"Computador jogou {itens[jogadapc]}")
print(f"Jogador jogou {itens[jogada]}")
print("-=" * 10)

# Lógica para determinar o vencedor
if (jogadapc == 0 and jogada == 2) or (jogadapc == 1 and jogada == 0) or (jogadapc == 2 and jogada == 1):
    print("Computador vence!")
elif (jogada == 0 and jogadapc == 2) or (jogada == 1 and jogadapc == 0) or (jogada == 2 and jogadapc == 1):
    print("Jogador vence!")
elif jogada == jogadapc:
    print("Empate!")
else:
    print("Jogada inválida!")

