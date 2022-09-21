#Scrit que juega a piedra, papel o tijera
import random
#Leer eleccion del Usuario
user = input("Elige: piedra, papel o tijera\n")
#Generar eleccion de maquina 
aleatorio = random.randint(1,3)
if aleatorio == 1:
    machine = "piedra"
elif aleatorio == 2:
    machine = "papel"
else:
    machine = "tijera"
#Comparar para determinar quien gana
print(f"El usuario eligio {user} y la maquina elegio {machine}")

if machine == "piedra" and user == "piedra":
        print("Es empate")
elif machine == "piedra" and user == "papel":
        print("Ganas tu")
elif machine == "piedra" and user == "tijera":
        print("pierdes tu")
elif machine == "papel" and user == "piedra":
        print("Gana la maquina")
elif machine == "papel" and user == "papel":
        print("Empate")
elif machine == "papel" and user == "tijera":
        print("ganas tu")
elif machine == "tijera" and user == "piedra":
        print("Ganas tu")
elif machine == "tijera" and user == "papel":
        print("Gana la maquina")
else:
        print("Empate")


