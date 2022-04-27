

class nodoCola():
    info, sig = None, None


class Cola():

    def __init__(self):
        self.__frente = None
        self.__final = None
        self.__tamanio = 0
    
    def arribo(self, dato):
        nodo = nodoCola()
        nodo.info = dato

        if self.__final is None:
            self.__frente = nodo
        else:
            self.__final.sig = nodo
        self.__final = nodo

        self.__tamanio += 1

    def atencion(self):
        dato = self.__frente.info

        self.__frente = self.__frente.sig
        if self.__frente is None:
            self.__final = None


        self.__tamanio -= 1
        return dato



    def tamanio(self):
        return self.__tamanio


    def cola_vacia(self):
        return self.__frente is None

    def en_frente(self):
        return self.__frente.info

    def mover_al_final(self):
        dato = self.atencion()
        self.arribo(dato)
        return dato

# c = Cola()
# c.arribo(1)
# c.arribo(2)
# print('tamanio', c.tamanio())
# print(c.atencion())
# print('tamanio', c.tamanio())
# print(c.atencion())
# print('tamanio', c.tamanio())
# c.arribo(3)
# print('tamanio', c.tamanio())
# print(c.atencion())

c = Cola()

# from random import randint

# for i in range(10):
#     c.arribo(randint(0,100))

# for i in range(c.tamanio()):
#     print (c.mover_al_final())

# print('Tamaño', c.tamanio())


