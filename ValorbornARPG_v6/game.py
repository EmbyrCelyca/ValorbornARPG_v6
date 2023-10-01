import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, alpha
from world_gen import World
from player import Player
from skills_engine import SkillsEngine
from interpolation import lerp
from hotkey_manager import HotkeyManager
from basic_skills import DashSkill


# Initialize Pygame
pygame.init()

# Set up the display
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Valorborn')

clock = pygame.time.Clock()
FPS = FPS  # Import this from settings

# Initialize world
world = World()

# Initialize player
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Create a SkillsEngine instance for the player
player_skills_engine = SkillsEngine(player)
player_skills_engine.initialize_available_skills()

# Register DashSkill
player_skills_engine.register_skill('Dash', DashSkill)

# Create a HotkeyManager instance and pass the SkillsEngine instance to it
hotkey_manager = HotkeyManager(player_skills_engine)

# Map skills to keys
player_skills_engine.map_skill_to_key('dash', pygame.K_SPACE)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            player.update(mouse_x, mouse_y)
  
    # Calculate alpha based on the time elapsed between frames
    dt = clock.tick(FPS) / 1000.0  # Convert milliseconds to seconds
    alpha = 1.0 - (1.0 / (1.0 + dt))  # You can adjust this formula
 
    # Move player towards mouse cursor when LMB is pressed or held
    mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position outside the event loop
    if pygame.mouse.get_pressed()[0]:
        player.move_towards(mouse_x, mouse_y)

    # Game logic here
    mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position outside the event loop
    print("Calling activate_skills")
    player_skills_engine.activate_skills(mouse_x, mouse_y)

    # Draw everything
    world.draw_background(window)  # Draw the background
    world.draw_grid(window, player.x, player.y, alpha)  # Draw the grid
    world.draw_origin(window)  # Draw the origin
    player.draw(window)  # Draw the player
    
    pygame.display.update()
    clock.tick(FPS)
