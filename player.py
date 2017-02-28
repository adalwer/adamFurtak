import pygame
from time import sleep
from Chopin import chopin
import random

class player:
    sounds = []
    S = ["" for i in range (8)]
    def __init__ (self):
        pygame.init ()
        
        self.S [0] = "C1.aiff"
        self.S [1] = "D1.aiff"
        self.S [2] = "E1.aiff"
        self.S [3] = "F1.aiff"
        self.S [4] = "G1.aiff"
        self.S [5] = "A1.aiff"
        self.S [6] = "B1.aiff"
        self.S [7] = "C2.aiff"
        
    def play (self,i, j):
        pygame.mixer.music.load (self.S[i])
        pygame.mixer.music.play()
        sleep (j)



#end of player

C = chopin ()
P = player()
tab = C.getMelody (100);
for i in range (100):
    P.play (tab [i].hight, tab [i].lenght / 7)
