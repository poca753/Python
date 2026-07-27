n = c = s = 0  # Inicializa as variáveis
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:  # Condição de parada
        break
    c += 1  # Incrementa o contador de números
    s += n  # Soma os valores digitados
print(f'A soma dos {c} valores foi {s}!')