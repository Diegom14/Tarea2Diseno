import timeit
import random

# Se crea la clase item la cual tiene el peso y precio de cada uno.
class Item:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight
 
    def __str__(self):
        return "Precio: %d - Peso: %d" % (self.price, self.weight)
    
    def __repr__(self):
        return self.__str__()


#Funcion para crear objetos con peso y precio aleatorio.
def ItemAleatorio(n):
      items = [0]  * n
      for i in range(n):
          items[i] = Item(random.randint(1, 10), random.randint(1, 10)) 
      return items
print ("ingrese la cantidad de objetos: ")      
k = input()
items = []
items = ItemAleatorio(k)


#Funcion que resuelve el problema
def transporte(items, capacity):

    sumas = [[0 for j in range(capacity + 1)]
           for i in range(len(items) + 1)]
    
    itemUsado = [[0 for j in range(capacity + 1)]
           for i in range(len(items) + 1)]
    
    
    for i, item in enumerate(items, start=1):
        for j in range(1, capacity + 1):
            if item.weight <= j:
                if item.price + sumas[i][j - item.weight] >= sumas[i - 1][j]:
                    sumas[i][j] = item.price + sumas[i][j - item.weight]
                    itemUsado[i][j] = 1
                else:
                    sumas[i][j] = sumas[i - 1][j]
            else:
                sumas[i][j] = sumas[i - 1][j]
                
    itemsParaLlevar = []
    n = len(items)
    while n > 0 and capacity >= 0:
        if itemUsado[n][capacity]==1:
            itemsParaLlevar.append(items[n-1])
            capacity -= items[n-1].weight
        n -= 1
    return itemsParaLlevar


print("ingrese la capacidad del transporte: ")
W = input()
print transporte(items, W)               
countWeight = 0
countPrice = 0
for i in transporte(items, W):
    countWeight += i.weight
    countPrice += i.price
print "Peso total: ", countWeight, "Precio total: ", countPrice 

times = 1   
tiempo = timeit.Timer(lambda: transporte(items, W), "")
tiempof = tiempo.repeat(times, 1)
print tiempof
