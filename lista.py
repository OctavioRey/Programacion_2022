

class nodoLista(object):
    info, sig = None, None


class Lista(object):


    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0


    def insertar(self, dato):
        nodo = nodoLista()
        nodo.info = dato

        if (self.__inicio is None) or (nodo.info < self.__inicio.info) :
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and nodo.info > actual.info):
                anterior = anterior.sig
                actual = actual.sig
            
            #No importa si es el ultimo nodo o no
            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def lista_Vacia(self):
        return self.__inicio is None

    def tamanio(self):
        return self.__tamanio

    def barrido(self):

        aux = self.__inicio
        while (aux is not None):
            print (aux.info)
            aux = aux.sig
    
    def busqueda(self, buscado):
        pos = None
        aux = self.__inicio
        while (aux is not None and pos is None):
            if(aux.info == buscado):
                pos = aux
            aux = aux.sig

    def eliminar(self, clave):
        dato = None
        if(self.__inicio.info == clave):
            dato = self.__inicio.info
            self.__inicio = self.__inicio.sig
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and actual.info < clave):
                anterior = anterior.sig
                actual = actual.sig

            if (actual is not None and actual.info == clave):
                dato = actual.info
                anterior.sig = actual.sig
        return dato

    def modificar(self, viejo, nuevo):
        pos = self.eliminar(viejo)
        if pos is not None:
            self.insertar(nuevo)


l = Lista()

from random import randint

l.insertar(10)
l.insertar(7)
l.insertar(13)
l.insertar(15)
l.insertar(8)
l.insertar(1)

l.modificar(7, 19)

l.barrido()


