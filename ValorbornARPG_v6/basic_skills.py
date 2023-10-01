# basic_skills.py
# This module defines the basic skills available to entities in the game.
# Each skill is implemented as a class that inherits from BaseSkill.
import pygame
from base_skill import BaseSkill
from attributes import Attributes
from settings import FPS

class BasicSkills:
    def __init__(self, entity):
        print("Initializing BasicSkills...") 
        self.entity = entity  # Reference to the entity (player or enemy) using the skills




