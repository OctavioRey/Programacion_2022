def factorial_recursivo(n):
    if (n == 0):
        return 1
    else:
        return n * factorial_recursivo(n-1)

# print (factorial_recursivo(5))

def FibonacciR(n):
    if (n == 0 or n == 1):

        return n
    else:
        return FibonacciR(n-1) + FibonacciR(n-2)

#print (FibonacciR(7))



# Hacer ejercicios 2 4 6 7 10 20


#Ejercicio 2

def sumatoria(n):
    if (n == 0):
        return n
    else:
        return n + (sumatoria(n-1))

# print (sumatoria(5))


#Ejercicio 4

def potenciaR(base, exponente):
    if (exponente == 0):
        return 1
    else:
        return base * potenciaR(base, exponente-1)

#print (potenciaR(4,3))

#Ejercicio 6

def invertirR(string, indice):
    if (indice == 1):
        return string[indice-1]
    else:
        return string[indice-1] + invertirR(string, indice-1)

cadena = "kekw"

#print (invertirR(cadena, len(cadena)))

def invertirR_mejorado(string):
    if (len(string) == 0):
        return string
    else:
        return string[-1] + invertirR_mejorado(string[:-1])

#print (invertirR_mejorado(cadena))

#Ejercicio 7

def algoritmoR(n):
    if (n == 1):
        return n
    else:
        return 1/n + algoritmoR(n-1)

# print (algoritmoR(3))

#Ejercicio 10

def contadorR(n):
    if (n < 10):
        return 1
    else:
        return 1 + (contadorR(n // 10))

#print (contadorR(457))

#Ejercicio 20

Lista = [10, 5, 7, 13, 20, 32]


def busqueda_secuencialR(vector, buscado, posicion):
    if (posicion == len(vector)):
        return -1
    elif(buscado == vector[posicion]):
        return posicion
    else:
        return (busqueda_secuencialR(vector, buscado, posicion + 1))

#print (busqueda_secuencialR(Lista, 21, 0))

def busqueda_secuencialMejorada(vector, buscado):
    if (len(vector) == 0):
        return -1
    elif(buscado == vector[-1]):
        return len(vector)-1
    else:
        return busqueda_secuencialMejorada(vector[:-1], buscado)

#print (busqueda_secuencialMejorada(Lista, 20))

#Ejercicio 21

lista_ordenada = [0, 1, 2, 3, 4, 5, 6]

def busqueda_binariaR(vector, buscado, primero, ultimo):
    med = (primero + ultimo) // 2

    if (primero > ultimo):
        return -1
    elif(buscado == vector[med]):
        return med
    elif (vector[med] < buscado):
        return busqueda_binariaR(vector, buscado, med+1, ultimo)
    else:
        return busqueda_binariaR(vector, buscado, primero, med-1)

# print (busqueda_binariaR(lista_ordenada, 6 , 0, len(lista_ordenada) -1))


matriz = [
    [1, 2, 3],
    [3, 4, 5],
    [6, 7, 8]
    ]

#for i in range(3):
#    for j in range(3):
#        print (matriz[i][j])

for i in range(3):
    print (matriz[i])


 


