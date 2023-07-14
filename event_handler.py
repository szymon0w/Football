import pygame
import sys

class EventHandler:
    def __init__(self):
        self.move_x = 0
        self.move_y = 0

    #used to handle events sent from users
    def handle_events(self):
        
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_RIGHT:
                            self.move_x = 10
                        case pygame.K_LEFT:
                            self.move_x = -10   
                        case pygame.K_UP:
                            self.move_y = -10
                        case pygame.K_DOWN:
                            self.move_y = 10
                case pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.move_x = 0  
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.move_y = 0 
   
        return self.move_x, self.move_y          
               

    
