

class nodoLista(object):
    info, sig = None, None


class Lista(object):


    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0


    def insertar(self, dato):
        nodo = nodoLista()
        nodo.info = dato

        if self.__inicio is None:
            self.__inicio = nodo
        elif(nodo.info < self.__inicio.info):
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