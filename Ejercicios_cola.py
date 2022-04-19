from cola import Cola

#Ejercicio 1
# vocales = ["A", "E", "I", "O", "U"]

# def random_character():
#     from random import randint
#     return chr(randint(65,90)) #! mayuscula

# c = Cola()


# for i in range(20):
#     dato = random_character()
#     c.arribo(dato)

# for i in range(c.tamanio()):
#     dato = c.atencion()
#     if (dato not in vocales):
#         c.arribo(dato)
#     else:
#         print('dato eliminado', dato)

# print()

# for i in range(c.tamanio()):
#     print (c.mover_al_final())


#Ejercicio 6

# elemento_contar = input("Ingrese la letra que desea contar: ")
# contador = 0

# for i in range(c.tamanio()):
#     if (elemento_contar == c.mover_al_final()):
#         contador += 1

# print("La cantidad de ocurrencias es: ", contador)



#Ejercicio 10

c = Cola()
c_2 = Cola()

class Notificacion():
    hora, aplicacion, mensaje = None, None, None

Aplicaciones = ["Facebook", "Twitter", "Instagram"]
Hora = ["11:43", "15:57", "12:30", "09:20"]
Mensaje = ["Python", "Nuevo Amigo", "Hola"]

from random import choice

for i in range(5):
    dato = Notificacion()
    dato.aplicacion = choice(Aplicaciones)
    dato.hora = choice(Hora)
    dato.mensaje = choice(Mensaje)
    c.arribo(dato)

for i in range(c.tamanio()):
    dato = c.mover_al_final()
    print (dato.aplicacion)

    #Punto 1
# def Borrar_Facebook(cola):
#     for i in range(cola.tamanio()):
#         dato = cola.atencion()
#         if (dato.aplicacion != "Facebook"):
#             cola.arribo(dato)


# print()
# Borrar_Facebook(c)

    #Punto 2
# def Mostrar_Twitter(cola):
#     for i in range (cola.tamanio()):
#         dato = cola.mover_al_final()
#         if ((dato.aplicacion == "Twitter") and (dato.mensaje == "Python")):
#             print(dato.hora, dato.aplicacion, dato.mensaje)
            
# print()
# Mostrar_Twitter(c)
# print()
# for i in range(c.tamanio()):
#     dato = c.mover_al_final()
#     print (dato.aplicacion, dato.hora, dato.mensaje)
    
    #Punto 3

# print()
# contador = 0

# for i in range(c.tamanio()):
#     dato = c.mover_al_final()
#     if ((dato.hora == "11:43") or (dato.hora == "15:57")):
#         c_2.arribo(dato)
#         contador += 1

# for i in range(c_2.tamanio()):
#     dato = c_2.mover_al_final()
#     print (dato.aplicacion, dato.hora, dato.mensaje)

# print ("La cantidad de notificaciones en la segunda pila es de: ", contador)