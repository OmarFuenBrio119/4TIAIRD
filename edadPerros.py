#Lee la edad de alguien
edad = input("Ingresa cuantos años tienes: ")
#Restar 2 a esa edad y se llame last_name
last_name = int(edad) - 2
#first_years sera igual a los 2 por 10.5
first_years = 10.5 * 2
#Multiplicamos los años restantes (last_name) por 4
x = last_name*4
#Sumar los first_years con el resultado anterior
suma = first_years + x
#Imprimir los siguientes "Tienes 24 años que equivalen a 78 años perrunos"
print(f"Tienes {edad} años que equivalen a {suma} años perrunos")