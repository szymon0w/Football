import pygame
from image_handler import ImageHandler
from event_handler import EventHandler
from game_engine import GameEngine
from controller.controller import Controller
import config

print("Before playing choose game type:\n \'1\' - 1 vs 1 (WSAD and arrows)\n \'2\' - 1 vs 1 (controller and arrows)")
control_type = input()
# Define some colors
clock = pygame.time.Clock()
pygame.init()
event_handler = EventHandler()
game_engine = GameEngine()
image_handler = ImageHandler()
pygame.display.set_caption("Football")
 
# Loop until the user clicks the close button. 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
if control_type == "2":
    controller = Controller() 
# -------- Main Program Loop -----------
while True:
    
    # --- Main event loop
    player_moves = event_handler.handle_events()
    if control_type == "2":
        roll, pitch, yaw = controller.getRotations()
        player_moves[0] = [2 * yaw * config.PLAYER_SPEED, 2* roll * config.PLAYER_SPEED]
    # --- Game logic should go here
    players, ball, points = game_engine.game_loop(player_moves)

    # --- Drawing code should go here
    image_handler_parameters = image_handler.update(players, ball, points)
    clock.tick(60)
