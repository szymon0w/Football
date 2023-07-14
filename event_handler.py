import pygame
import sys
import config

class EventHandler:
    def __init__(self):
        self.player_moves = [[0, 0], [0, 0]]

    #used to handle events sent from users
    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_d:
                            self.player_moves[0][0] = config.PLAYER_SPEED
                        case pygame.K_a:
                            self.player_moves[0][0] = -config.PLAYER_SPEED   
                        case pygame.K_w:
                            self.player_moves[0][1] = -config.PLAYER_SPEED
                        case pygame.K_s:
                            self.player_moves[0][1] = config.PLAYER_SPEED
                        case pygame.K_RIGHT:
                            self.player_moves[1][0] = config.PLAYER_SPEED
                        case pygame.K_LEFT:
                            self.player_moves[1][0] = -config.PLAYER_SPEED   
                        case pygame.K_UP:
                            self.player_moves[1][1] = -config.PLAYER_SPEED
                        case pygame.K_DOWN:
                            self.player_moves[1][1] = config.PLAYER_SPEED
                case pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.player_moves[1][0] = 0  
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.player_moves[1][1] = 0 
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.player_moves[0][0] = 0  
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        self.player_moves[0][1] = 0 
   
        return self.player_moves         
               

    
