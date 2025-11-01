#Ejercicio 1
def imprimir_hola_mundo():
    return "Hola, Mundo!"

#Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola, {nombre}!"

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} de edad y vivo en {residencia}."
    
#Ejercicio 4
def calcular_area_circulo(radio):
    area = 3.14 * radio ** 2
    return f"El área del círculo de radio {radio} es: {area}"

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return f"El perímetro del círculo de radio {radio} es: {perimetro}"

#Ejercicio 5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return f"{segundos} segundos son {horas} horas."

#Ejercicio 6
def tabla_multiplicar(numero):
    resultado = []
    for i in range(1, 11):
        resultado.append(f"{numero} x {i} = {numero * i}")
    return "\n".join(resultado)

#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error (división por cero)"

    return f"Suma: {suma}\nResta: {resta}\nMultiplicación: {multiplicacion}\nDivisión: {division}"

#Ejercicio 8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return f"El Índice de Masa Corporal (IMC) es: {imc}"

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}°C son {fahrenheit}°F"

#Ejercicio 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return f"El promedio de {a}, {b} y {c} es: {promedio}"

#FIN