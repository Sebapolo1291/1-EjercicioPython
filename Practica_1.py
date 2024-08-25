'''Realizar una función que se llame separar() que reciba una lista de nros y
devuelva dos listas ordenadas. La primera con nros pares y la segunda con
nros impares.'''

# se crea la funcion
def separar(lista):
    numeros_pares = []
    numeros_impares = []

    for n in lista: #condicion para saber si los numeros son pares e impares
        if n % 2 == 0:
            numeros_pares.append(n) #append agrega un item al final de la lista
        else:
            numeros_impares.append(n)#append agrega un item al final de la lista


    return sorted(numeros_pares), sorted(numeros_impares)
#sorted ordena los valores
#return devuelve valores pares e impares

valores = input("Ingrese una lista de numeros separados por comas (ejemplo:20, 23, 43): ")
lista = [int(n) for n in valores.split(',')]

#lista = [0,0,0] se utiliza para almacenar varios valores
#split define el separador que el usuario va a poder utilizar cuando ingrese los valores
#int(n) que tipo de valor va a utilizar

