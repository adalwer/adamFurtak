from perlin import Perlin
import random

class sound:
    lenght = int (0)
    hight = int (0)
    
    def makeSound (len, high):
        S = sound ()
        S.lenght = len
        S.hight = high
        return S


class chopin:
    tactLenght = int (0)
    lastLenght = int (0)
    mn = float (10000.0)
    mx = float (0)
    lenghts = []

    P = Perlin ()

    previous = int (0)
    Stala = float ()

    def __init__ (self):
        self.Stala = random.random ()
        self.tactLenght = 16
        self.lastLenght = self.tactLenght
        for i in range (5):
            self.lenghts.append (pow(2,i))

    def getSound (self):
        tempLenght = int ()
        while (True):
            tempLenght = self.lenghts [random.randrange (0, 5)]
            if tempLenght <= self.lastLenght:
                self.lastLenght -= tempLenght
                break
        if (self.lastLenght == 0):
            self.lastLenght = self.tactLenght
        self.previous += tempLenght    
        if (self.previous * self.Stala > 30):
            self.previous = 0
            self.Stala = random.random ()
        temp = self.previous * self.Stala
        return sound.makeSound (tempLenght, int(self.P.getValue (0, temp) * 10) )
    #end of getSound method

    def getMelody (self, lenght):
        arr = []
        for i in range (lenght):
            arr.append (self.getSound ())
        return arr
            
        
#end_of_chopin























































