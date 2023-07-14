import pygame
from image_handler import ImageHandler
from event_handler import EventHandler
from game_engine import GameEngine

# Define some colors

clock = pygame.time.Clock()
pygame.init()
event_handler = EventHandler()
game_engine = GameEngine()
image_handler = ImageHandler()

# Set the width and height of the screen [width, height]
 
pygame.display.set_caption("Football")
 
# Loop until the user clicks the close button. 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while True:
    
    # --- Main event loop
    move_x, move_y = event_handler.handle_events()

    # --- Game logic should go here
    player, ball, points = game_engine.game_loop(move_x, move_y)

    # --- Drawing code should go here
    image_handler_parameters = image_handler.update(player, ball, points)
    clock.tick(60)
