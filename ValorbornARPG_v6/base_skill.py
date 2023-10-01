# base_skill.py

from attributes import Attributes

class BaseSkill:
    def __init__(self, entity):
        self.entity = entity  # Reference to the entity (player or enemy) using the skill

    def use(self):
        pass  # Define the skill behavior in subclasses
