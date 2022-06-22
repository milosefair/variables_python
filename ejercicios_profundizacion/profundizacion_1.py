# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia



- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''


# Empezar aquí la resolución del ejercicio

from pickle import FALSE, TRUE


print('¡Nuestra primera calculadora!')

condicion = TRUE

while condicion == TRUE:

  print  ("Seleccione la letra de la operación que quiera realizar:\n" "A) Suma \n" "B) Resta \n" "C) Multiplicación \n" "D) División \n" "E) Exponente/Potencia")

  operacion= str(input()).upper()

  if operacion == "A":

    print ("escriba el primer número a sumar")
    numero_1 = float(input())

    print ("escriba el segundo número a sumar")
    numero_2 = float(input())

    suma = numero_1 + numero_2

    print ("el resultado de sumar ", numero_1, "y", numero_2, "es ", suma, "\n")

  if operacion == "B":

    print ("escriba el primer número para restar")
    numero_1 = float(input())

    print ("escriba el segundo númer que va a restar")
    numero_2 = float(input())

    resta = numero_1 - numero_2

    print ("el resultado de restar ", numero_1,"-", numero_2, "es: ", resta, "\n")

  if operacion == "C":

    print ("escriba el primer número a multiplicar")
    numero_1 = float(input())

    print ("escriba el segundo número a multiplicar")
    numero_2 = float(input())

    multi = numero_1 * numero_2

    print ("el resultado es de multiplicar ", numero_1,"x", numero_2, "es: " , multi, "\n")

  if operacion == "D":

    print ("escriba el primer número para dividir")
    numero_1 = float(input())

    print ("escriba el segundo número a sumar")
    numero_2 = float(input())

    divi = numero_1 / numero_2

    print ("el resultado es de dividir ", numero_1,"/", numero_2, "es: " , divi, "\n")

  if operacion == "E":

    print ("escriba el primer número")
    numero_1 = float(input())

    print ("escriba el exponente")
    numero_2 = float(input())

    expo = numero_1 ** numero_2

    print ("el resultado es de  ", numero_1,"elevado al ", numero_2, "es: " , expo, "\n")

  else:
    print ("la letra no corresponde a una operación \n")
 
  print ("Desea realizar otra operación?, responda SI o NO \n")

  respuesta= str(input()).upper()

  if respuesta == "NO":
    condicion = FALSE
    print ("gracias por usar la calculadora \n")

  if respuesta == "SI":
    condicion = TRUE

  else:
    condicion = FALSE
    print ("gracias por usar la calculadora \n")











