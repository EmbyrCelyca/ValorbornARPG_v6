import pygame
from base_skill import BaseSkill
from attributes import Attributes
from settings import FPS

class BasicSkills:
    def __init__(self, entity):
        print("Initializing BasicSkills...") 
        self.entity = entity  # Reference to the entity (player or enemy) using the skills
        self.dash_skill = DashSkill(entity)
        print(f"Dash skill initialized: {self.dash_skill}")

    def update(self):
        # Update the cooldown timer
        if self.entity.dash_cooldown_timer > 0:
            self.entity.dash_cooldown_timer -= 1 / FPS

            # Reset the dash flag when the cooldown is complete
            if self.entity.dash_cooldown_timer <= 0:
                self.entity.is_dashing = False


class DashSkill(BaseSkill):
    def use(self, target_x, target_y):
        print("Dash skill activated")
        if not self.entity.is_dashing and self.entity.dash_cooldown_timer <= 0:
            # Calculate the movement vector for the dash
            dx = target_x - self.entity.x
            dy = target_y - self.entity.y
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance != 0:
                normalized_dx = dx / distance
                normalized_dy = dy / distance

                dash_dx = self.entity.dash_distance * normalized_dx
                dash_dy = self.entity.dash_distance * normalized_dy

                # Apply the dash movement with adjusted cast speed and duration
                self.entity.x += dash_dx * Attributes().cast_speed
                self.entity.y += dash_dy * Attributes().cast_speed

                # Set the skill duration and flag
                self.entity.skill_duration_timer = Attributes().skill_duration
                self.entity.is_dashing = True
                
                self.entity.dash_cooldown_timer = 3
                
    def register(cls, skill_registry):
        skill_registry["dash"] = cls

