
def bublesort(lista):

    n = len(lista)
    #print(n)


    for i in range(n-1):
        # range(n) tambien funciona, el bucle externo se repetira una vez mas
        for x in range(0, n-i-1):
            if lista[x] > lista[x+1]:
                lista[x], lista[x+1] = lista[x+1], lista[x]


ordenamiento = [45, 35, 3, 2, 68, 5, 8, 10]
bublesort(ordenamiento)

print(ordenamiento)

for i in range(len(ordenamiento)):
    print("%d" %ordenamiento[i])