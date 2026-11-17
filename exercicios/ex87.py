par = []
impar = []

for c in range(0, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

par.sort()
impar.sort()
print(f'Os valores pares em ordem crescente foram {par} e os ímpares {impar}')
