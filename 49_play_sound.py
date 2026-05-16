import pygame

pygame.init()
pygame.mixer.init()

#music load
pygame.mixer.music.load("sound.mp3")
#music play 
pygame.mixer.music.play()

input("Press Enter to exit")