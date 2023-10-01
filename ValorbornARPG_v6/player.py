import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from attributes import Attributes  # Import Attributes class
from movement import MovementHandler
from skills_engine import SkillsEngine



class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = (0, 128, 255)
        self.attributes = Attributes()  # Initialize Attributes for the player
        self.movement_handler = MovementHandler(5)  # Initialize with move_speed
        self.is_dashing = False
        self.dash_cooldown_timer = 0
        self.dash_distance = 100  # You can set this to whatever value you like
        
    def draw(self, window):
        pygame.draw.rect(window, self.color, (SCREEN_WIDTH // 2 - self.width // 2, SCREEN_HEIGHT // 2 - self.height // 2, self.width, self.height))

    def update(self, target_x, target_y):
        # Update the cooldown timer
        if self.dash_cooldown_timer > 0:
            self.dash_cooldown_timer -= 1 / FPS

            # Reset the dash flag when the cooldown is complete
            if self.dash_cooldown_timer <= 0:
                self.is_dashing = False
        pass

    def move_towards(self, target_x, target_y):
        dx = target_x - (SCREEN_WIDTH // 2)
        dy = target_y - (SCREEN_HEIGHT // 2)
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance != 0:
            normalized_dx = dx / distance
            normalized_dy = dy / distance

            # Scale speed based on distance to cursor
            half_screen_distance = (SCREEN_WIDTH ** 2 + SCREEN_HEIGHT ** 2) ** 0.5 / 2
            speed_scale = min(distance / half_screen_distance, 1)
            scaled_speed = self.attributes.move_speed * speed_scale

            self.x += scaled_speed * normalized_dx
            self.y += scaled_speed * normalized_dy
