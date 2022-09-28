from email import message
from email.errors import MessageError

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1/num2

if __name__ == '__main__':
    message = f"calculadora: \n Elige una opcion\n1 - suma\n2 - resta\n3 - multiplicar\n4 - divide\n"
    while True:
        opcion = int(input(message))
        #comparar cada una de las opciones y llamar a la funcion correcta 
        if opcion == 1:
            resultado_suma = suma(23, 66)
            print("El resultado de la suma es", resultado_suma)
        elif opcion == 2:
            resultado_resta = resta(23, 66)
            print("El resultado de la resta es", resultado_resta)
        elif opcion == 3:
            resultado_multiplicar = multiplicar(23, 66)
            print("El resultado de la multiplicacion es", resultado_multiplicar)
        elif opcion == 4:
            resultado_divide = divide(23, 66)
            print("El resultado de la division es", resultado_divide)
        elif opcion == 5:
            print('Bye!!')
            break
        else:
            print("Opcion Incorrecta")
