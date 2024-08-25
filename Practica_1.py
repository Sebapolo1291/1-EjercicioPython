''' Realizar una función que se llame area_rectangulo() que devuelva
el área del rectángulo a partir de su base y altura.'''

#se utiliza la palabra DEF para definir como funcion la siguiente variable
def area_rectangulo (base, altura): #Se escribe la función
    multiplicacion = base * altura  #Se escribe la operacion
    return multiplicacion #el return para que devuelva el valor

base = float(input("Ingrese Base del triangulo")) 
#Se le pide al usuario que ingrese los valores
#tambien se agrega el tipo de dato
altura = float(input("Ingrese la Altura del triangulo"))

resultado = area_rectangulo (base, altura)
#se agrego una variable para poder imprimir el resultado en pantalla

print(f"El Area del rectángulo es {resultado}")
#se imprime el resueltado en la pantalla

