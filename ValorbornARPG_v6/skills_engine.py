# skills_engine.py
# This module defines the SkillsEngine class, which manages the skills available to an entity.
# It handles skill registration, key mapping, and skill activation.
import pygame
from basic_skills import BasicSkills  # Import the BasicSkills class

class SkillsEngine:
    
    def __init__(self, entity=None):
        
            self.entity = entity
        
            self.available_skills = {}  # Store instances of available skills
        
            self.skill_key_mapping = {}  # Default skill-key mapping

    def update_skills(self):
        for skill_instance in self.available_skills.values():
            if hasattr(skill_instance, 'update_cooldown'):
                skill_instance.update_cooldown()
                
        self.available_skills = {}  # Store instances of available skills
        print("SkillsEngine initialized")

    def initialize_available_skills(self):
        print("Initializing available skills...")
        # Initialize basic skills for the player
        basic_skills = BasicSkills(self.entity)
        print(f"Available skills after initialization: {self.available_skills}")  # Debug


    def register_skill(self, skill_key, skill_class):
        self.skill_registry[skill_key] = skill_class


    def activate_skills(self, target_x, target_y):
        self.update_skills()  # Update the state of each skill
        print(f"Available skills: {self.available_skills}")
        print(f"Current skill-key mapping: {self.skill_key_mapping}")
        keys = pygame.key.get_pressed()
        print(f"Keys pressed: {keys}")