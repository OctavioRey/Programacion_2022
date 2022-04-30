#Ejercicios 16(sin prioridad), 18 y 22.

from cola import Cola
from random import randint

#Ejercicio 18

cola_1 = Cola()
cola_2 = Cola()
Criterio = ["A", "C", "F"]
cont_1 = 0
cont_2 = 0

        #Punto A (Cambiar a 1000 el rango del ciclo FOR)
for i in range(10):
    dato = chr(randint(65,70)) + str(randint(0,999))
    cola_1.arribo(dato)

        #Punto B
for i in range(cola_1.tamanio()):
    dato = cola_1.atencion()
    if (dato[0] not in Criterio):
        cola_2.arribo(dato)
    else:
        cola_1.arribo(dato)

        #Punto C

if (cola_1.tamanio() > cola_2.tamanio()):
    print ("La cola 1 tiene mayor cantidad de turnos.")
else:
    print ("La cola 2 tiene mayor cantidad de turnos.")


for i in range(cola_1.tamanio()):
    print (cola_1.mover_al_final())

print()

for i in range(cola_2.tamanio()):
    print (cola_2.mover_al_final())
