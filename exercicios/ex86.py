tamp = []
princ = []
mai = men = 0
while True:
    tamp.append(str(input('nome: ')))
    tamp.append(float(input('peso: ')))
    if len(princ) == 0:
        mai = men = tamp[1]
    else:
        if tamp[1] > mai:
            mai = tamp[1]
        if tamp[1]<men:
            men = tamp[1]

    princ.append(tamp[:])
    tamp.clear
    resp = str(input("quer continuar? ")).lower().strip()[0]
    if resp == "n":
            break
print(f" os dados foram {princ} ")
print(f"voce cadastrou {len(princ)} pessoas")
print(f"o maior peso foi de {mai} kg. peso de ", end='')
for p in princ:
     if p[1] == mai:
          print(f"[{p[0]}]", end='')
print(f"o menor peso foi de {men} kg. peso de ", end='' )
for p in princ:
     if p[1] == men:
          print(f"[{p[0]}]", end='')
