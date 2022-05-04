from lista import Lista
from random import randint

def random_character():
    from random import randint
    return chr(randint(65,90)) #! mayuscula

#Ejercicio 2

# Lista1 = Lista()
# Vocales = ["A", "E", "I", "O", "U"]

# for i in range (10):
#     Lista1.insertar(random_character())


# Lista1.barrido()

# print()

# for vocal in Vocales:
#     aux = Lista1.eliminar(vocal)
#     while(aux is not None):
#         aux = Lista1.eliminar(vocal)

# Lista1.barrido()


#Ejercicio 3

Lista_1 = Lista()
Lista_2 = Lista()

for i in range (10):
    Lista_1.insertar(randint(0,10))


Lista_1.barrido()
print()
print(Lista_1.obtener_elemento(3))
# Lista_1.insertar_en_posicion(4,58)
# print()
# Lista_1.barrido()