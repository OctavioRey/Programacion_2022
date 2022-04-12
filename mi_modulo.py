


def suma (n1, n2):
    "Esta funcion devuelve la suma de dos numeros"
    return n1 + n2

vector = [11, 3, 81, 7, 45, 100, 5, -1, 32, 9]

def quicksort(vec, primero, ultimo):
    pivot = ultimo
    izq = primero
    der = ultimo - 1

    while(izq < der):
        while((vec[izq] < vec[pivot])  and (izq <= der)):
            izq += 1
        while ((vec[der] > vec[pivot]) and (der >= izq)):
            der -= 1
        if (izq < der):
            vec[izq], vec[der] = vec[der], vec[izq]
    if (vec[izq] > vec[pivot]):
        vec[izq], vec[pivot] = vec[pivot], vec[izq]
        
    if (primero < izq):
        quicksort(vec, primero, izq-1)
    if (ultimo > izq ):
        quicksort(vec, izq+1, ultimo)


quicksort(vector, 0, len(vector)-1)

print(vector)
