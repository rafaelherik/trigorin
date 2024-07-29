import os
import yaml

class ConfigLoader:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance._initialized = False            
            cls._instance.config = {}         
            cls._instance.__load_default_config() 
        return cls._instance
    
    def __load_default_config(self):
        config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
    
    def load_config(self, config_file):
        config_path = config_file
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def get_config(self, key, default=None):
        keys = key.split('.')
        value = self.config
        for k in keys:
            if value and k in value:
                value = value[k]
            else:
                return default
        return value

config_loader = ConfigLoader()