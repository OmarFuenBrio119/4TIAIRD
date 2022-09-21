#Condicionales if elif else 
#Nos permiten evaluar expresiones booleanas que de cumplirse realizan
#Una accion y en caso de que no entoces realizan otra 

genre = input("ingresa tu genero: 1.- hombre 2.- mujer ")
#Evaluar si es una persona es mayor de edad 
age = int(input('Ingresa tu edad: '))


if age < 2:
    if genre == "1":
        print("Eres un bebe!!")
    else:
        print("Eres una bebe")
elif age < 12:
    if genre == "1":
        print("Eres un niño!!")
    else:
        print("Eres una niña")
elif age < 18:
    if genre == "1":
        print("Eres un joven!!")
    else:
        print("Eres una joven")
elif age < 50:
   if genre =="1":
        print("Eres un adulto!!")
   else:
        print("Eres una adulta")
else:
         print('Eres muy mayor')