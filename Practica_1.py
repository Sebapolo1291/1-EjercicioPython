'''Realizar una función que se llame intermedio() que a partir de dos nros
devuelva el punto intermedio. Ej. El punto intermedio
entre 10 y 24 = 17; entre 12 y 50 = 31.'''
#se crea una funcion
def intermedio(valor1, valor2):
    suma = valor1 + valor2
    division = suma / 2
    return division
# se le pide a los usuarios que ingrese valores
valor1 = int(input("Ingrese un valor: "))
valor2 = int(input("Ingrese un valor: "))

#variables para mostrar en la impresion de pantalla
valor_intermedio = intermedio(valor1, valor2)

#se muestran los valores por pantalla
print(f"el valor intermedio de {valor1} y {valor2} es {valor_intermedio}")

