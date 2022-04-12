

class nodoPila():
    info , sig = None, None
    
class Pila():

    def __init__(self):
        self.__tamanio = 0
        self.__cima = None

    def tamanio(self):
        return self.__tamanio

    def apilar(self, dato):
        nodo = nodoPila()
        nodo.info = dato
        if(self.__cima is None):
            self.__cima = nodo
        else:
            nodo.sig = self.__cima
            self.__cima = nodo
        
        self.__tamanio += 1

    def cima(self):
        return self.__cima.info , self.__cima.sig

    def pila_vacia(self):
        return self.__cima is None

    def desapilar(self):
        dato = self.__cima.info
        self.__cima = self.__cima.sig
        self.__tamanio -= 1
        return dato

#from random import randint

#pila1 = Pila()
#print(pila1.pila_vacia())

#for i in range(10):
#    num = randint(0,100)
#    print("numero generado: ", num)
#    pila1.apilar(num)

#print (pila1.tamanio())

#while (not pila1.pila_vacia()):
#    dato = pila1.desapilar()
#    print("elemento desapilado: ", dato)

#print (pila1.pila_vacia())
#print()