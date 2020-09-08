import os

EXCLUDED_MODULES = ["BaseModel", "__init__"]

dirname = os.path.dirname(__file__)

__all__ = []
for f in os.listdir(dirname):
    base, ext = os.path.splitext(f)
    if ext == ".py" and base not in EXCLUDED_MODULES:
        __all__.append(base)
