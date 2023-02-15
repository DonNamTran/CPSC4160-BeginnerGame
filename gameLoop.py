import pygame, sys, model, eventController
from view import *
from eventController import *
from model import *


class gameLoop:
    pygame.init()
    def __init__(self):
        print("what up")

        model = Model()
        view = View(model)
        events = EventController(model, view)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            view.updateScreen()
            events.move_object(model.player_gameRect)



#Main method that starts the gameLoop
def main():
    gameLoop()

if __name__ == "__main__":
    main()