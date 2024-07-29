from os.path import dirname, basename, isfile, join
import glob
from suvorin.config.config_loader import ConfigLoader



modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py") and not f.endswith("config_loader.py")]

print(f"modules: {modules}")
print(f"all: {__all__.__dict__}")

