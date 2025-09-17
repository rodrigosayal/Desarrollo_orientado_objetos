from abc import ABC, abstractclassmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
        self.posicion = 0
    
    @abstractclassmethod
    def caminar (self):
        self.posicion

    

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