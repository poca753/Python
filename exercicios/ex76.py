from random import randint
randomN =   [randint(0, 100) for _ in range(5)]
tupla = randomN
print(f'Os numeros aleatórios são: {randomN}')
print(f'O maior numero sorteado foi: {max(tupla)}') #A função max() retorna o maior valor de uma tupla ou lista
print(f'O menor numero sorteado foi: {min(tupla)}') #A função min() retorna o menor valor de uma tupla ou lista