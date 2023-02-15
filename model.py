import pygame, sys

class Model:
    player_rectColor = (200, 0, 0)
    player_rectSize = rectWidth, rectHeight = 100, 100
    player_rectPos = rectX, rectY = 350, 350
    player_rectSpeed = 1

    player_gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)

    def __init__(self):
        pass