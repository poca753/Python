numeros = (
int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: '))
)
print(f'Os numeros digitados foram {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print(f'O valor 3 foi digitado na posição {numeros.index(3)+1}')
pares = [n for n in numeros if n % 2 == 0]
if pares:
    print(f' Os números pares digitados foram: {pares}')
else:
    print('Não foram digitados nenhum numero par')