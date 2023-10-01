# hotkey_manager.py

class HotkeyManager:
    def __init__(self, skills_engine):
        print("HotkeyManager initialized")
        self.skills_engine = skills_engine
        self.key_mapping = {}  # Mapping of keys to skill_keys
        self.key_states = {}  # Track the state of each key
        print(self.key_mapping)
        
    def map_skill_keys(self, key_mapping):
        for key, skill_key in key_mapping.items():
            self.key_mapping[key] = skill_key
        print(f"Current key mappings: {self.key_mapping}")

    def activate_mapped_skill(self, key):
        print(f"Trying to activate skill mapped to key: {key}")
        skill_key = self.key_mapping.get(key)
        if skill_key:
            self.skills_engine.activate_skill(skill_key)

    def check_key_state(self, key):
        return self.key_states.get(key, False)

    def set_key_state(self, key, state):
        self.key_states[key] = state
        
