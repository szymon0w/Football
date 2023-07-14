import pygame
import config

size = (config.WIDTH, config.HEIGHT)


class ImageHandler:
    def __init__(self):
        self.screen = pygame.display.set_mode(size)

    #updating the screen
    def update(self, player, ball):
        # --- Screen-clearing code goes here
        self.screen.fill(config.BLACK)
    
        # --- Drawing code should go here
        pygame.draw.circle(surface = self.screen, center = (player.x, player.y), color = config.WHITE, radius = player.radius)
        pygame.draw.circle(surface = self.screen, center = (ball.x, ball.y), color = config.WHITE, radius = ball.radius)
    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
        # --- Limit to 60 frames per second
