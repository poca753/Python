from random import randint
from time import sleep
aleatorio = randint(0,5)
print("vou pensar em um numero entre 0 e 5. Tente adivinhar...")
jogador = int(input("em que numero eu pensei"))
print("pensando")
sleep(3)
if aleatorio == jogador
else:
    print("ganhei eu pensei em {} e não o {}".format(aleatorio,jogador))