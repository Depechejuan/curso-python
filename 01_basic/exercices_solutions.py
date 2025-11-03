from os import system
if system("clear") != 0: system("cls")
print("--------------")
print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")
print("Juan")
print("Alicante")
print("--------------")
print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None
print(f"Tipo variable a: {type(a)}, variable b: {type(b)}, variable c: {type(c)}, variable d: {type(d)}, variable e: {type(e)}")
print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

cadena = "12345"
cadena = int(cadena)
print(type(cadena))
cadena = float(cadena)
print(type(cadena))
cadena = 3.99
cadena = int(cadena)
print(type(cadena))
print(cadena)
#ha redondeado

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")
nombre = "Juan"
edad = 39
altura = 1.79
print(f"Me llamo {nombre} tengo {edad} años y mido {altura}")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi = 3.1416
redondeo = round(pi)
resultado = redondeo / 2
print(resultado)