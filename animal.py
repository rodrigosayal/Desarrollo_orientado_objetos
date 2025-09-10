from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def hablar (self):
        pass

    

class Perro(Animal):

    def hablar(self):
        print("wow wow")

class Gato(Animal):

    def hablar(self):
        print("miau miau")