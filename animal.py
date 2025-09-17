import random
import time
import os


class Caballo(object):
    def __init__(self, name, f ,t):
        self.name = name
        self.posicion = 0
        self.f = f
        self.t = t
    
    def corre(self, ):
     p =   random.randint(self.f, self.t)
     self.posicion = self.posicion + p

    def dibuja(self):
        x = ("_" * self.posicion)  + f"[{self.name}]"
        print(x)

pista = [Caballo ("Yatasto", 1 , 5),
         Caballo ("MAga", 1 , 5),
         Caballo ("Pedro",1 , 5),
         Caballo ("Feca", 1 , 6),
         Caballo ("Gogo", 1 , 5),
         Caballo ("Lizz", 1 , 5),
         ]        

termino = False


while not termino:
   i = 0
   os.system('cls')
   while i < len(pista):
      pista[i].corre()
      pista[i].dibuja()
      if pista[i].posicion > 100:
         termino = True
      i = i + 1 
   
   time.sleep(0.5)