nombre = input("¿Cómo te llamas? \n")
print(f"Hoola {nombre}")

age = int(input("¿Cuántos años tienes?"))
print(f"Dentro de 20 años tendrás {age + 20} años")

print("Obtener multiples valores a la vez")
country, city = input("¿En qué país y ciudad vives? \n").split()
print(f"Vives en {country}, {city}")