

def lonelyinteger(a):
    for i in a:
        filtrado = len(list(filter(lambda x: x == i, a)))
        if int(filtrado) == 1:
            return i
    #return num






print(lonelyinteger([1,1,2,1,1,2,3,4,3,4,4,8,3]))