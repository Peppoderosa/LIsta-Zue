'''
import pygame

pygame.init()
pygame.mixer.music.load('frog.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
'''

import playsound

playsound.playsound('frog.mp3')