from cola import Cola

#Ejercicio 1
vocales = ["A", "E", "I", "O", "U"]

def random_character():
    from random import randint
    return chr(randint(65,90)) #! mayuscula

c = Cola()


for i in range(20):
    dato = random_character()
    c.arribo(dato)

for i in range(c.tamanio()):
    dato = c.atencion()
    if (dato not in vocales):
        c.arribo(dato)
