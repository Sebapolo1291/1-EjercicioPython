'''Realizar una función que se llame relacion() que a partir de dos nros
realice lo siguiente:
a. Si el primer nro es mayor que el segundo, devuelve 1
b. Si el primer nro es menor que el segundo, devuelve -1
c. Si ambos nros son iguales, devuelve 0 '''


# se creo una funcion llamada relacion
def relacion(numero1, numero2):
    if numero1 > numero2: #si el primero valor es mayor devuelve 1
        return 1
    elif numero1 < numero2:#si el primero valor es menor devuelve -1
        return -1
    else:                  #si los valores son iguales devuelve 0
        return 0

numero1 = int(input("Ingrese un valor: ")) #Se el solicita al usuario un valor
numero2 = int(input("Ingrese un valor: ")) #Se el solicita al usuario un valor

valor = relacion(numero1, numero2) #variable para mostrar en el resultado final


print(f"El resultado es: {valor}")  #Imprime el resultado en pantalla

