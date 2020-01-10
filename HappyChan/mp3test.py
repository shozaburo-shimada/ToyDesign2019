import pygame.mixer
import time

pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(1) #loop count

time.sleep(20) #20byousaisei
pygame.mixer.music.stop() #teishi

