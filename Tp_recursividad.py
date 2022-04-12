# El ejercicio de la mochila es similar a la busqueda secuencial


#Ejercicio 5





# def romano_a_decimal(decimal):
#    Romanos = {
#    "I" : 1,
#    "V" : 5,
#    "X" : 10,
#    "L" : 50,
#    "C" : 100,
#    "D" : 500,
#    "M" : 1000,
#}
#    resultado = 0




#Ejercicio 22

mochila = ["Cigarrillo", "Pera", "Basura", "Sable de Luz", "Linterna"]

cont = 0

def usar_la_fuerza(vector, contador):

    if len(vector) == 0:
        return "El sable de luz no esta en la mochila"
    else:
        if (vector[0] == "Sable de Luz"):
            return "Encontraste el sable de luz y se sacaron ", contador, "objetos"
        else:
            contador += 1
            return usar_la_fuerza(vector[1:], contador)


print (usar_la_fuerza(mochila, cont))
