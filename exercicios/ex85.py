expr = input('Digite uma expressão: ')
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()  # Remove o último '(' aberto
        else:
            pilha.append(')')  # Marca o erro (fechou sem abrir)
            break

if len(pilha) == 0:
    print('A expressão está correta!')
else:
    print('A expressão não está correta!')
