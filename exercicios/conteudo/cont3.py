top = input("qual seu nome ")
print("prazer em conhecelo {:20}!".format(top))#espçamento
print("prazer em conhecelo {:>20}!".format(top))#espaçamento pra direita
print("prazer em conhecelo {:<20}!".format(top))#espaçamento pra esquerda
print("prazer em conhecelo {:^20}!".format(top))#alinhamento no centro

va1 = int(input("digite um valor "))
va2 = int(input("digite outro valor "))
soma = (va1+va2)#criar variavel quando utilizar em outra parte do codigo
print("a soma é {}".format(soma))