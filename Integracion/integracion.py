
#Ejercicio Integrador Python
# Ejercicio 1- El maximo comun divisor

print("Ejercicio 1- El maximo comun divisor\n")

def maximocd(divisor, dividendo):
    while dividendo:
        divisor, dividendo = dividendo, divisor % dividendo
    return divisor

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = maximocd(num1, num2)
print(f"El máximo común divisor entre {num1} y {num2} es {resultado}\n\n")

# Ejercicio 2- El maximo comun divisor
print("Ejercicio 2- El maximo comun divisor\n")

def calcular_mcm(a, b):
    
    producto = a * b
    mcd = maximocd(a, b)
    mcm = producto // mcd
    
    return mcm


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

mcm = calcular_mcm(numero1, numero2)
print(f"El mínimo común múltiplo entre {numero1} y {numero2} es {mcm}\n\n")

# Ejercicio 3- Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario 
# con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

print("Escriba una oracion y devuelva un diccionario\n")
print("con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).\n\n")

def contar_palabras(cadena):
    palabras = cadena.split()  
    diccionario = {}
    
    for palabra in palabras:
        palabra = palabra.lower()  
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    
    return diccionario

cadena = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(cadena)

for palabra, frecuencia in resultado.items():
    print(f"'{palabra}': {frecuencia}")
    
print("Este fue el resultado final del ejercicio\n\n")

# Ejercicio 4 - Escribir una función que reciba una cadena de caracteres y devuelva un diccionario 
# con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más 
# repetida y su frecuencia.
print("Debera ingresar una frase, se le mostrara un diccionario con cantidad de veces que ocurren\n")
print("y luego una dupla con las palabras y sus repeticiones")
def contar_palabras(cadena):
    palabras = cadena.split()  
    diccionario = {}
    
    for palabra in palabras:
        palabra = palabra.lower()  
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    
    return diccionario

def palabra_mas_repetida(diccionario):
    palabra_max = None
    frecuencia_max = 0
    
    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia
    
    return palabra_max, frecuencia_max

cadena = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(cadena)
palabra, frecuencia = palabra_mas_repetida(resultado)

print("Diccionario de palabras y frecuencias:")
for palabra, frecuencia in resultado.items():
    print(f"'{palabra}': {frecuencia}")

print(f"Palabra más repetida: '{palabra}' con frecuencia {frecuencia}\n\n")

# Ejercicio 5 - Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario 
# y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera 
# iterativa como recursiva.
print("Ingrese un valor entero\n")
def get_int():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("Error: Ingrese un valor entero válido.")

valor_entero = get_int()
print(f"Valor entero ingresado: {valor_entero}\n")

# Ejercicio 6 - Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
#       Un constructor, donde los datos pueden estar vacíos.
#           Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#                mostrar(): Muestra los datos de la persona.
#                Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

print('Se contruye el objeto Persona y se lo instancia con valore fijos que se mostraran en pantalla\n')
class Persona:
    def __init__(self, nombre="", edad=None, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        if edad is not None and edad < 0:
            print("Error: La edad debe ser un valor positivo.")
        else:
            self.edad = edad
    
    def get_dni(self):
        return self.dni
    
    def set_dni(self, dni):
        if len(dni) != 9:
            print("Error: El DNI debe tener 9 dígitos.")
        else:
            self.dni = dni
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")
    
    def es_mayor_de_edad(self):
        return self.edad >= 18 if self.edad is not None else False


persona1 = Persona()
persona1.set_nombre("Juan")
persona1.set_edad(25)
persona1.set_dni("123456789")
persona1.mostrar()
print("Es mayor de edad:", persona1.es_mayor_de_edad(),"\n\n")

# Ejercicio 7- Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
# titular (que es una persona) y cantidad (puede tener decimales). 
# El titular será obligatorio y la cantidad es opcional. 
# Crear los siguientes métodos para la clase:  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, 
# sólo ingresando o retirando dinero.  mostrar(): Muestra los datos de la cuenta.  ingresar(cantidad): se 
# ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.  retirar( retirar(cantidad): 
# se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Persona:
    def __init__(self, nombre="", edad=None, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
class Cuenta(Persona):
    def __init__(self, titular, cantidad=0.00):
        self.titular = titular
        self.cantidad = cantidad
    
    def get_titular(self):
        return self.titular
    
    def get_cantidad(self):
        return self.cantidad
    
    def mostrar(self):
        print(f'Titular: {titular.nombre}, DNI: {titular.dni}')
        numero_formateado = f"{self.cantidad:.2f}"
        print("Cantidad en la cuenta:", numero_formateado)
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad

titular = Persona("Juan", 30, "123456789")
cuenta1 = Cuenta(titular, 1000.0)
cuenta1.mostrar()

cuenta1.ingresar(500)
cuenta1.retirar(200)
cuenta1.mostrar()


