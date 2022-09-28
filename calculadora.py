from email import message
from email.errors import MessageError
import os

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1/num2

def return_values():
    num1 = int(input("Selecciona un numero: "))#pedir numero
    num2 = int(input("Selecciona otro un numero: "))#pedir otro numero
    return [num1, num2] #regresar umeros 

if __name__ == '__main__':
    message = f"calculadora: \n Elige una opcion\n1 - suma\n2 - resta\n3 - multiplicar\n4 - divide\n"
    while True:
        opcion = int(input(message))
        #comparar cada una de las opciones y llamar a la funcion correcta 
        if opcion == 1:
            #Pedir numeros al usuario  
            numeros = return_values()
            resultado_suma = suma(numeros[0], numeros[1])
            print("El resultado de la suma es", resultado_suma)
        elif opcion == 2:
            #Pedir numeros al usuario 
            numeros = return_values()
            resultado_resta = resta(numeros[0], numeros[1])
            print("El resultado de la resta es", resultado_resta)
        elif opcion == 3:
            #Pedir numeros al usuario 
            numeros = return_values()
            resultado_multiplicar = multiplicar(numeros[0], numeros[1])
            print("El resultado de la multiplicacion es", resultado_multiplicar)
        elif opcion == 4:
            #Pedir numeros al usuario 
            numeros = return_values()
            resultado_divide = divide(numeros[0], numeros[1])
            print("El resultado de la division es", resultado_divide)
        elif opcion == 5:
            print('Bye!!')
            break
        else:
            print("Opcion Incorrecta")



clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()
