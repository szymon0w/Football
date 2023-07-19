import pygame
import config

size = (config.WIDTH, config.HEIGHT)


class ImageHandler:
    def __init__(self):
        self.screen = pygame.display.set_mode(size)
        self.bg = pygame.image.load('static/pitch.jpg').convert()
        self.bg = pygame.transform.scale(self.bg, (config.WIDTH, config.HEIGHT))


    #updating the screen
    def update(self, players, ball, points):
        # --- Screen-clearing code goes here
        self.screen.blit(self.bg, (0, 0))

        font = pygame.font.SysFont('chalkduster.ttf', 72)
        img = font.render(f'{points[0]} : {points[1]}', True, config.WHITE) 
          
        # --- Drawing code should go here
        pygame.draw.circle(surface = self.screen, center = (ball.x, ball.y), color = config.GRAY, radius = ball.radius)
        for player in players: 
            pygame.draw.circle(surface = self.screen, center = (player.x, player.y), color = player.color, radius = player.radius)
        pygame.draw.line(surface = self.screen, color = config.RED, start_pos = (config.WIDTH, config.GOAL_SIZE[0]), end_pos = (config.WIDTH, config.GOAL_SIZE[1]), width = 10) 
        pygame.draw.line(surface = self.screen, color = config.GREEN, start_pos = (0, config.GOAL_SIZE[0]), end_pos = (0, config.GOAL_SIZE[1]), width = 10) 
        self.screen.blit(img, (config.WIDTH * 0.85, config.HEIGHT // 20))


    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
        # --- Limit to 60 frames per second
