

from pila import Pila

from random import randint

#Ejercicio 1


pila1 = Pila()
pila_aux = Pila()


def random_character():
    from random import randint
    return chr(randint(0, 90))


#for i in range (10):
#    dato = randint(0,10)
#    print ("El dato apilado es: ", dato)
#    pila1.apilar(dato)


#x = int(input("Ingrese el numero que desea contar ocurrencias: "))
#contador = 0
#while (not pila1.pila_vacia()):
#    dato = pila1.desapilar()
#
#    if (dato == x):
#        contador += 1

#print ("La cantidad de veces que se repitió el número fue: ", contador)


#Ejercicio 2


#for i in range (10):
#    dato = randint(0,100)
#    print ("El dato apilado es: ", dato)
#    pila1.apilar(dato)

#while (not pila1.pila_vacia()):
#    dato = pila1.desapilar()

#    if (dato % 2) == 0:
#        pila_aux.apilar(dato)

#print()

#while (not pila_aux.pila_vacia()):
#    dato = pila_aux.desapilar()
#    pila1.apilar(dato)

#while (not pila1.pila_vacia()):
#    dato = pila1.desapilar()
#    print(dato)



#Ejercicio 3

#for i in range(5):
#    dato = randint(0, 10)
#    print ("El elemento apilado es: ", dato)
#    pila1.apilar(dato)

#numero_a_quitar = int(input("Ingrese el numero que desee quitar: "))
#numero_a_reemplazar = int(input("Ingrese el numero por el cual quiere reemplazarlo: "))


#while (not pila1.pila_vacia()):
#    dato = pila1.desapilar()
#    
#    if dato == numero_a_quitar:
#        pila_aux.apilar(numero_a_reemplazar)
#    else:
#        pila_aux.apilar(dato)

#while (not pila_aux.pila_vacia()):
#    dato = pila_aux.desapilar()
#    pila1.apilar(dato)
#print()

#while (not pila_aux.pila_vacia()):
#    dato = pila_aux.desapilar()
#    print(dato)


# Ejercicio 5

#pila1 = Pila()
#pila_aux2 = Pila()
#pila_invertida = Pila()


#palabra = input("Ingrese una palabra: ")

#for letra in palabra:
#    pila1.apilar(letra)


#while (not pila1.pila_vacia()):
#    dato = pila1.desapilar()
#    pila_invertida.apilar(dato)
#    pila_aux2.apilar(dato)

#while (not pila_aux2.pila_vacia()):
#    pila1.apilar(pila_aux2.desapilar())


#while (not pila1.pila_vacia() and (pila1.cima() == pila_invertida.cima())):
#    pila1.desapilar()
#    pila_invertida.desapilar()



#if (pila1.pila_vacia()):
#    print ("Es palíndromo")
#else:
#    print("No es palindromo", pila1.tamanio())





#Ejercicio 11


#for i in range(15):
#    caracter = random_character()
#    print(caracter)
#    pila1.apilar(caracter)

#Ejercicio 13

# class Trajes():
#     traje, pelicula, estado = None, None, None

# trajes = ['Mark I', 'Mark II', 'Mark IV', 'Mark V', 'Mark X', 'Mark XLIV']
# peliculas = ['Iron Man I','Iron Man II', 'Iron Man III', 'Avengers1', 'Spider-Man: Homecoming', 'Capitan America: Civil War']
# estado = ['Dañado', 'Impecable', 'Destruido']

# pila2 = Pila()

# from random import choice

# for i in range (len(trajes)):
#     dato = Trajes()
#     dato.traje = trajes[i]
#     dato.pelicula = peliculas[i]
#     dato.estado = choice(estado)
#     pila1.apilar(dato)
#     pila_aux.apilar(dato)


# pelicula = input('Ingrese la pelicula en la que se uso el traje Mark LXXXV: ')
# insertar = True
# while (not pila1.pila_vacia()):
#     dato = pila1.desapilar()
#         #Punto A
#     if dato.traje == "Mark XLIV":
#         print('El traje fue usado en la pelicula: ', dato.pelicula)
#         #Punto B
#     if (dato.estado == "Dañado"):
#         print(f'El modelo {dato.traje} resulto dañado')
#         #Punto F
#     if (dato.pelicula in ['Spider-Man: Homecoming' , 'Capitan America: Civil War']):
#         print (f'El modelo {dato.traje} fue utilizado en la pelicula  {dato.pelicula}')
#         #Punto E
#     if (dato.traje == 'Mark LXXXV' and dato.pelicula == pelicula):
#         insertar = False
#         #Punto C
#     if (dato.estado != 'Destruido'):
#         pila2.apilar(dato)

#     #print(dato.traje, dato.pelicula, dato.estado)

# while (not pila2.pila_vacia()):
#     pila1.apilar(pila2.desapilar())

# if(insertar):
#     dato = Trajes()
#     dato.traje = 'Mark LXXXV'
#     dato.pelicula = pelicula
#     dato.estado = choice(estado)
#     pila1.apilar(dato)

# print()

# while(not pila1.pila_vacia()):
#     dato = pila1.desapilar()
#     print(dato.traje, dato.estado, dato.pelicula)




# 14  FUNCIONA


# for i in range (7):
#     dato = randint(0,10)
#     print(dato)
#     if (pila1.pila_vacia()):
#         pila1.apilar(dato)
#     elif (dato < pila1.cima()):
#         while ((not pila1.pila_vacia() and dato < pila1.cima())):
#             pila_aux.apilar(pila1.desapilar())
#         pila1.apilar(dato)
#         while (not pila_aux.pila_vacia()):
#             pila1.apilar(pila_aux.desapilar())

#     else:
#         pila1.apilar(dato)




# print()

# while (not pila1.pila_vacia()):
#     dato = pila1.desapilar()
#     print (dato)

# print()

# while (not pila_aux.pila_vacia()):
#     dato = pila_aux.desapilar()
#     print (dato)


#Ejercicio 16    FUNCIONA

pila_V = Pila()
pila_VII = Pila()
pila_aux = Pila()
pila_encontrados = Pila()


personajes_V = ["Leia", "Luke Skywalker", "Anakin Skywalker", "Obi-Wan Kenobi", "Jabba"]
personajes_VII = ["Leia", "Pepega", "Luke Skywalker", "Jabba", "General Grievous"]


for i in range(len(personajes_V)):
    dato = personajes_V[i]
    pila_V.apilar(dato)

for i in range(len(personajes_VII)):
    dato = personajes_VII[i]
    pila_VII.apilar(dato)


while (not pila_V.pila_vacia()):
    dato = pila_V.desapilar()

    if (dato == pila_VII.cima()):
        print('xD')
    else:
        print('Lmao')


# print()
# while (not pila_V.pila_vacia()):
#     dato = pila_V.desapilar()
#     print (dato)



# print()

# while (not pila_VII.pila_vacia()):
#     dato = pila_VII.desapilar()
#     print(dato)
