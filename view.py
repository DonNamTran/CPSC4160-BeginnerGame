import pygame, sys

class View:
    SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
    surface = pygame.display.set_mode(SCREEN_SIZE)
    
    model = ""
    #Screen and rectangle properties. 
    screenColor = (255, 255, 255)
    def __init__(self, model):
        #Creates the font objects 
        self.timer_font = pygame.font.Font('freesansbold.ttf', 32)
        self.timer_font.bold = True

        self.model = model
        pygame.display.set_caption("Object Dodger")
        

    #method that updates all the objects in the screen.
    def updateScreen(self):
        self.surface.fill(self.screenColor)
        pygame.draw.rect(self.surface, self.model.player_rectColor, self.model.player_gameRect)

        #renders and updates the timer
        self.timer_text = self.timer_font.render("Score: " + str(pygame.time.get_ticks()), True, (0,0,0), (255, 255, 255))
        self.surface.blit(self.timer_text, (0, 0))
        pygame.display.update()
    