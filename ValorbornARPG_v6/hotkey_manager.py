# hotkey_manager.py
import pygame
from settings import DEFAULT_HOTKEYS
# This module defines the HotkeyManager class, which manages the mapping of keys to skills.

class HotkeyManager:
    def __init__(self, skills_engine):
# Initializes the HotkeyManager with a reference to the SkillsEngine and empty key mappings.
        print("HotkeyManager initialized")
        self.skills_engine = skills_engine
        self.key_mapping = self.map_to_pygame_keys(DEFAULT_HOTKEYS)  # Mapping of keys to skill_keys
        self.key_states = {}  # Track the state of each key
    
    def update(self):
        keys = pygame.key.get_pressed()
        # Check only the keys that are mapped
        for key in self.key_mapping.keys():
            self.key_states[key] = keys[self.key_mapping[key]]
        pass  # Placeholder for the update method
        
    
    def map_to_pygame_keys(self, default_keys):
        pygame_key_mapping = {
            'space': pygame.K_SPACE,
            'lmb': pygame.BUTTON_LEFT,
            'rmb': pygame.BUTTON_RIGHT,
            'a': pygame.K_a,
            's': pygame.K_s,
            'd': pygame.K_d,
            'f': pygame.K_f,
            'g': pygame.K_g,
            'v': pygame.K_v,
            'left_shift': pygame.K_LSHIFT,
            'esc': pygame.K_ESCAPE
            }
        return {action: pygame_key_mapping[key] for action, key in default_keys.items()}
    def map_skill_keys(self, key_mapping):
# Maps skill keys to keyboard keys.
        for key, skill_key in key_mapping.items():
            self.key_mapping[key] = skill_key
        print(f"Current key mappings: {self.key_mapping}")


        
