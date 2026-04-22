nome = str(input("escreva uma palavra aleatoria")).strip().upper()
print("A letra A aparece {} vezes na frase".format(nome.count("A")))
print("a primeira letra A apareceu na posição{}".format(nome.find)) # +1 para ficar na posição correta da escrita desconsiderando o último
print("A última letra A apareceu na posição {}".format(nome.rfind("A")))  # procura da direita para esquerda
