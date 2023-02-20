import pygame, sys

class Model:

    #all the attributes related to the player_rectangle.
    player_rectColor = (200, 0, 0)
    player_rectSize = rectWidth, rectHeight = 70, 70
    player_rectPos = rectX, rectY = 350, 350
    player_rectSpeed = 1
    player_gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)

    def __init__(self):
        pass