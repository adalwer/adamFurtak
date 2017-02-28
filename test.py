import pygame.mixer
from time import sleep

pygame.mixer.init()
pygame.mixer.music.load("A1.aiff")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)
sleep (.2)
pygame.mixer.music.stop();

pygame.quit()