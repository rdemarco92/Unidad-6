#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo")

#Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} de edad y vivo en {residencia}.")
    
#Ejercicio 4
def calcular_area_circulo(radio):
    area = 3.14 * radio ** 2
    print(f"El área del círculo de radio {radio} es: {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    print(f"El perímetro del círculo de radio {radio} es: {perimetro}")

#Ejercicio 5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos son {horas} horas.")

#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error (división por cero)"
    
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")

#Ejercicio 8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"El Índice de Masa Corporal (IMC) es: {imc}")

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C son {fahrenheit}°F")

#Ejercicio 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de {a}, {b} y {c} es: {promedio}")

#FIN