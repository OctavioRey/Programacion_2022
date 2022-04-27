#Ejercicio 5

# Romanos = {
#    "I" : 1,
#    "V" : 5,
#    "X" : 10,
#    "L" : 50,
#    "C" : 100,
#    "D" : 500,
#    "M" : 1000,
# }




# def convertir_romano(numero):
#     if (len(numero) == 1):
#         return Romanos[numero[0]]
#     elif(Romanos[numero[0]] >= Romanos[numero[1]]):
#         return convertir_romano(numero[1:]) + Romanos[numero[0]]
#     elif(Romanos[numero[0]] < Romanos[numero[1]]):
#         return convertir_romano(numero[1:]) - Romanos[numero[0]]


# print (convertir_romano("XXIV"))




#Ejercicio 22

# mochila = ["Cigarrillo", "Pera", "Basura", "Sable de Luz", "Linterna"]

# cont = 0

# def usar_la_fuerza(vector, contador):

#     if len(vector) == 0:
#         return "El sable de luz no esta en la mochila"
#     else:
#         if (vector[0] == "Sable de Luz"):
#             return "Encontraste el sable de luz y se sacaron ", contador, "objetos"
#         else:
#             contador += 1
#             return usar_la_fuerza(vector[1:], contador)


# print (usar_la_fuerza(mochila, cont))

#Ejercicio 23

# def Mostrar(matriz):
#     print("Laberinto: ")
#     for fila in matriz:
#         for valor in fila:
#             print("\t", valor, end=" ")
#         print()

# matriz = [[1,1,0,1,0],
#           [1,1,1,1,0],
#           [1,1,1,1,0],
#           [1,0,1,0,0],
#           [1,0,1,1,1]]
          
# def salida(laberinto, x, y, tamanio_matriz):
#     if x == tamanio_matriz and y == tamanio_matriz:
#         laberinto[x][y] = 2
#         return True
#     else:
#         if x >= 0 and x <= 4 and y >= 0 and y <= 4 and laberinto[x][y] == 1:
#             laberinto[x][y] = 2
#             if salida(laberinto,x,y+1, tamanio_matriz) or salida(laberinto,x+1,y, tamanio_matriz) or salida(laberinto,x-1,y, tamanio_matriz) or salida(laberinto,x,y-1, tamanio_matriz):
#                 return True
#         else:
#             return False

# print(salida(matriz, 0, 0, len(matriz)-1))
# Mostrar(matriz)