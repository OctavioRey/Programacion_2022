def factorial_recursivo(n):
    if (n == 0):
        return 1
    else:
        return n * factorial_recursivo(n-1)

# print (factorial_recursivo(5))

def FibonacciR(n):
    if (n == 0 or n == 1):
        return n
    else:
        return n + FibonacciR(n-1)

print (FibonacciR(10))