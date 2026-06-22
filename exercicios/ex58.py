soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher_20 = 0

for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    soma_idade += idade
    
    # Lógica para o homem mais velho
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
        
    # Lógica para mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        tot_mulher_20 += 1

media = soma_idade / 4

print(f'\nA média de idade do grupo é de {media} anos.')
if nome_velho != '':
    print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.')
else:
    print('Não foram registrados homens no grupo.')
print(f'Ao todo são {tot_mulher_20} mulheres com menos de 20 anos.')
