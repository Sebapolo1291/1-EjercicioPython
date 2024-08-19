
# 1 Definir dos variables de distinto valor numérico, realizar una operación y mostrar el resultado por pantalla

numero1 = 10
numero2 = 5
resultado = numero1 + numero2  # Realizamos una suma
print("La suma de", numero1, "y", numero2, "es:", resultado) #se imprime el resultado de la suma de las dos variables numericas

# 2 Definir dos variables con diferentes cadenas de texto que se concatenen y finalmente se
muestren por pantalla.

cadena1 = "Hola esta es mi primera prueba"
cadena2 = "en Python"

# Concatenar las cadenas
resultado = cadena1 + cadena2

# Mostrar el resultado
print(resultado)


Para solicitar al usuario que ingrese su nombre y DNI, y luego imprimir esos valores en un mensaje en Python, puedes seguir estos pasos. El siguiente código realiza estas tareas:

Solicita al usuario que ingrese su nombre y DNI.
Guarda los valores en variables.
Imprime un mensaje con el nombre y el DNI.
Aquí tienes el código en Python:

python
Copiar código
# Solicitar al usuario que ingrese su nombre
nombre = input("Por favor, ingrese su nombre: ")

# Solicitar al usuario que ingrese su DNI
dni = input("Por favor, ingrese su DNI: ")

# Imprimir el resultado
print(f"El nombre del usuario es {nombre} y su DNI es {dni}.")