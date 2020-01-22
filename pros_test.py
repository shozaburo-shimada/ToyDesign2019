import subprocess
import pygame
import time


pygame.mixer.init()

command = "sudo omxplayer --win '0 0 480 270' --vol -10000 video1.mp4"
proc = subprocess.Popen(command, shell=True, stdin = subprocess.PIPE)
print("playback video1.mp4")

pygame.mixer.music.load("music1.mp3")
pygame.mixer.music.play(1)
print("playback music1.mp3")

time.sleep(5)

pygame.mixer.music.stop()
print("stop music1.mp3")

pygame.mixer.music.load("music2.mp3")
pygame.mixer.music.play(1)
print("playback music3.mp3")

time.sleep(5)

proc.stdin.write('q')
proc.stdin.flush()
print("stop video1.mp4")


command = "sudo omxplayer --win '0 0 480 270' --vol -10000 video2.mp4"
proc = subprocess.Popen(command, shell=True, stdin = subprocess.PIPE)
print("playback video2.mp4")

time.sleep(5)

pygame.mixer.music.stop()
print("stop music2.mp3")

proc.stdin.write('q')
proc.stdin.flush()
print("stop video2.mp4")
