import os
import yaml


class ConfigLoader:

    _instance = None
    config_file = os.environ.get('SUVORIN_CONFIG_FILE')

    def __new__(cls, config_file='../../config.yaml'):
        if cls._instance is None:
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance._initialized = False
            cls._instance.config = {}
            cls._instance.load_config(config_file)
        return cls._instance

    def load_config(self, config_file):
        config_path = os.path.join(os.path.dirname(__file__), config_file)
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
