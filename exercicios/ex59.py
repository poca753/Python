sexo = str(input('Informe seu dados [m/f]: ')).strip().lower()[0]

while sexo not in 'mf':
    sexo = str(input('Dados inconsistentes, informe novamente: ')).strip().lower()[0]

print(f'O seu sexo é {sexo}')
