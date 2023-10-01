import pygame
from basic_skills import BasicSkills  # Import the BasicSkills class

class SkillsEngine:
    def __init__(self, entity):
        self.entity = entity
        self.skill_registry = {}  # Store registered skills
        self.skill_key_mapping = {}  # Mapping of keys to skills
        self.available_skills = {}  # Store instances of available skills
        print("SkillsEngine initialized")

    def initialize_available_skills(self):
        print("Initializing available skills...")
        # Initialize basic skills for the player
        basic_skills = BasicSkills(self.entity)
        print(f"Dash skill from BasicSkills: {basic_skills.dash_skill}")
        self.available_skills['dash'] = basic_skills.dash_skill
        print(f"Available skills after initialization: {self.available_skills}")  # Debug


    def register_skill(self, skill_key, skill_class):
        self.skill_registry[skill_key] = skill_class

    def map_skill_to_key(self, skill_key, key):
        print(f"Mapping {skill_key} to key {key}")
        self.skill_key_mapping[key] = skill_key

    def activate_skills(self, target_x, target_y):
        print(f"Available skills: {self.available_skills}")
        print(f"Current skill-key mapping: {self.skill_key_mapping}")
        keys = pygame.key.get_pressed()
        print(f"Keys pressed: {keys}")
        for key, skill_key in self.skill_key_mapping.items():
            if keys[key]:
                print(f"Activating skill: {skill_key}")
                skill_instance = self.available_skills.get(skill_key)
                if skill_instance:
                    print(f"Activating skill: {skill_key}")
                    skill_instance.use(target_x, target_y)