nome =str(input("qual o seu nome? "))
if nome == "daniel":
    print("que nome bonito")
elif nome == "paulo" or nome == "maria" or nome == "pedro":
    print("seu nome é bem popular no brasil")
elif nome in "ana claudia jessica juliana":
    print("que belo nome feminino")
else:
    print("seu nome é bem normal")