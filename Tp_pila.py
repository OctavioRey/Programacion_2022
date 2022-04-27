#Ejercicios 19 y 24

# from pila import Pila
# from random import choice, randint

# class Peliculas():
#     titulo, estudio, año = None, None, None

# Titulos = ["La Llamada", "Scream", "Scary-Movie", "Star-Wars", "Mi Pobre Angelito"]
# Estudios = ["Disney", "MGM", "Marvel Studios"]
# Años = ["2014", "2016", "2018", "1995"]



# pila1 = Pila()
# cont = 0
# for i in range (5):
#     dato = Peliculas()
#     dato.titulo = Titulos[i]
#     dato.estudio = choice(Estudios)
#     dato.año = choice(Años)
#     pila1.apilar(dato)

    #Punto A
# while (not pila1.pila_vacia()):
#     dato = pila1.desapilar()
#     if (dato.año == "2014"):
#         print (dato.titulo)

    #Punto B

# while (not pila1.pila_vacia()):
#     dato = pila1.desapilar()
#     if (dato.año == "2018"):
#         cont += 1
# print(cont)

    #Punto C

# while (not pila1.pila_vacia()):
#     dato = pila1.desapilar()
#     if ((dato.año == "2016") and (dato.estudio == "Marvel Studios")):
#         print (dato.titulo)


#Ejercicio 24

# class Personajes():
#     nombre, cant_pel = None, None

# Nombres = ["Rocket Raccoon", "Groot", "Daredevil", "Black Widow", "Capitan-America"]

# pila1 = Pila()
# pos = 0

# for i in range (5):
#     dato = Personajes()
#     dato.nombre = Nombres[i]
#     dato.cant_pel = randint(1,7)
#     pila1.apilar(dato)


    #Punto A

# while (not pila1.pila_vacia()):
#     dato = pila1.desapilar()
#     pos +=1
#     if ((dato.nombre == "Rocket Raccoon") or (dato.nombre == "Groot") ):
#         print (f'La posicion de {dato.nombre} en la pila es {pos}')

    #Punto B

# while (not pila1.pila_vacia()):
#     dato = pila1.desapilar()
#     if (dato.cant_pel > 5):
#         print (f'El personaje {dato.nombre} participó en {dato.cant_pel} peliculas')


    #Punto C

# while (not pila1.pila_vacia()):
#     dato = pila1.desapilar()
#     if (dato.nombre == "Black Widow"):
#         print (f'La {dato.nombre} participó en {dato.cant_pel} peliculas')

    
    #Punto D


# while (not pila1.pila_vacia()):
#     Inicial = ["C", "D", "G"]
#     dato = pila1.desapilar()
#     if (dato.nombre[0] in Inicial):
#         print (dato.nombre)
