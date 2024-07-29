from os.path import dirname, basename, isfile, join
import glob
from config_loader import ConfigLoader

config_loader = ConfigLoader()
config_loader.load_config('../config.yaml')
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")]

print(f"modules: {modules}")
print(f"all: {__all__.__dict__}")

