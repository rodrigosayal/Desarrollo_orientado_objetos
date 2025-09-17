from abc import ABC, abstractclassmethod

class Animal(ABC):
    def __init__(self, name, velocidad):
        self.name = name
        self.posicion = 0
        self.velocidad = velocidad
    
    
    def caminar (self, tiempo):
        self.posicion = self.velocidad * tiempo

    

class Perro(Animal):
    def __init__(self, name, ):
        super().__init__(name, 2)

class Gato(Animal):
    def __init__(self, name,):
        super().__init__(name, 1)


c = Perro("Rodro")
g = Gato("Pedro")

c.caminar(10)
g.caminar(10)

print(c.posicion)
print(g.posicion)



























"""
Eliminar tiempo y velocidad del ANIMAL
class Perro1(Animal):

    def __init__(self, name, velocidad):
        super().__init__(name)
        self.velocidad = velocidad
        
    def caminar(self): 
        self.posicion = self.posicion + self.velocidad   

class Perro2(Animal):

    def hablar(self):
        print("hola")
        
    def caminar(self): 
        self.posicion = self.posicion + self.velocidad   

p = Perro1 ("Cesar",2)
u = Perro2 ("Feca",1)
print(p.velocidad)
print(u.name)
"""