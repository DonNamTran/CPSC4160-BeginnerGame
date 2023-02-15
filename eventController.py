import pygame, sys

class EventController:
    model = ""
    view = ""
    def __init__(self, model, view):
        self.model = model
        self.view = view
        pass

    def move_object(self, gameObject):
        self.model.player_gameRect.clamp_ip(self.view.surface.get_rect())
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            print("up left pressed !!!")
            gameObject.move_ip(0,-self.model.player_rectSpeed)
            gameObject.move_ip(-self.model.player_rectSpeed,0)
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            print("up right pressed !!!")
            gameObject.move_ip(0,-self.model.player_rectSpeed)
            gameObject.move_ip(self.model.player_rectSpeed,0)
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            print("down left pressed !!!")
            gameObject.move_ip(0,self.model.player_rectSpeed)
            gameObject.move_ip(-self.model.player_rectSpeed,0)
        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            print("down right pressed !!!")
            gameObject.move_ip(0,self.model.player_rectSpeed)
            gameObject.move_ip(self.model.player_rectSpeed,0)
        elif keys[pygame.K_LEFT]:
            print("left pressed !!!")
            gameObject.move_ip(-self.model.player_rectSpeed,0)
        elif keys[pygame.K_RIGHT]:
            print("right pressed !!!")
            gameObject.move_ip(self.model.player_rectSpeed,0)
        elif keys[pygame.K_UP] and gameObject.y > 0:
            print("up pressed !!!")
            gameObject.move_ip(0,-self.model.player_rectSpeed)
        elif keys[pygame.K_DOWN]:
            print("down pressed !!!")
            gameObject.move_ip(0,self.model.player_rectSpeed)
        pass
        pass
    