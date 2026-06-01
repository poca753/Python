from random import randint
from time import sleep

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogada = int(input("Qual é a sua jogada? "))

jogadapc = randint(0, 2)

itens = ("Pedra", "Papel", "Tesoura")

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

print("-=" * 10)
print(f"Computador jogou {itens[jogadapc]}")
print(f"Jogador jogou {itens[jogada]}")
print("-=" * 10)

if (jogadapc == 0 and jogada == 1) or (jogadapc == 2 and jogada == 0) or (jogadapc == 1 and jogada == 2):
    print("Computador vence!")
elif (jogada == 0 and jogadapc == 1) or (jogada == 2 and jogadapc == 0) or (jogada == 1 and jogadapc == 2):
    print("Jogador vence!")
elif jogada == jogadapc:
    print("Empate!")
else:
    print("Jogada inválida!")

