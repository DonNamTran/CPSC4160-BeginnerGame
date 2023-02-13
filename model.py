import pygame, sys

#Window size
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800


pygame.init()
#pygame.display.init()
pygame.display.set_caption("yo what up")
surface = pygame.display.set_mode(SCREEN_SIZE)

#Screen and rectangle properties. 
screenColor = (255, 255, 255)
rectColor = (200, 0, 0)
rectSize = rectWidth, rectHeight = 100, 100
rectPos = rectX, rectY = 350, 350
rectSpeed = 1

gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)