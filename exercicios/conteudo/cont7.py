frase = (" curso de analise e desenvolvimento de sistemas ")
print(frase[6])#isso mostra o espaço na memoria
print(frase[6:34])#
print(frase[6:34:2])#pula de dois em dois
print(frase[:35])
print(frase[21:])
print(frase[17::28])
print(len(frase))
print(frase.count("s"))
print(frase.count("d",2))
print(frase.find("d"))
print(frase.find("android"))
print(frase[3]) #isso mostra o espaço da materia
print(frase[3:46]) #intervalo de caracteress menos o último
print(frase[3:45:2]) #pula de dois em dois
print(frase[3:45:2])
print(frase.replace('curso',"topete")) #troca a palavra
print(frase)
print(frase.upper()) #deixa maiusculo
print(frase.lower()) #deixa minusculo
print(frase.capitalize()) # deixa a primeira letra da primeira palavra maiusculo
print(frase.title()) #deixa todas a primeiras letras maiusculo
print(frase.strip()) #tira o espaço branco do inicio e final
print(frase.rstrip()) #tira o espaço em branco da direita
print(frase.lstrip()) #tira o espaço em branco da esquerda
print(frase.split()) #vai transformar o valor de comentario em uma lista
print("*".join(frase)) #voce uni um simbolo em cada parte so split