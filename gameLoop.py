import pygame, sys, model, eventController
from view import *
from eventController import *
from model import *


class gameLoop:
    pygame.init()
    def __init__(self):
        print("what up")

        #creates the mode, view, and events object
        model = Model()
        view = View(model)
        events = EventController(model, view)

        #game loop
        while True:

            #handles the player closing the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #calls the method in view that updates the screen. 
            view.updateScreen()

            #calls the method to move the player rectangle. 
            events.move_object(model.player_gameRect)



#Main method that starts the gameLoop
def main():
    gameLoop()

if __name__ == "__main__":
    main()