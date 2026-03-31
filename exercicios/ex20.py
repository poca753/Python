import math
ang = float(input("digite o angulo que deseja"))
seno = math.sin(math.radians(ang)) #os valores tem que ser em radianos então usamos math.radians
cose = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))
print("o angulo de {} tem seno de{:.2f}".format(ang,seno))
print("o angulo de {} tem coseno de {:.2f}".format(ang,cose))
print("o angulo de {} tem tangente de {:.2f}".format(ang,tang))