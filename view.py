import pygame, sys

class View:
    SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
    surface = pygame.display.set_mode(SCREEN_SIZE)
    model = ""
    #Screen and rectangle properties. 
    screenColor = (255, 255, 255)
    def __init__(self, model):
        self.model = model
        

    #method that updates all the objects in the screen.
    def updateScreen(self):
        self.surface.fill(self.screenColor)
        pygame.draw.rect(self.surface, self.model.player_rectColor, self.model.player_gameRect)
        pygame.display.update()
    