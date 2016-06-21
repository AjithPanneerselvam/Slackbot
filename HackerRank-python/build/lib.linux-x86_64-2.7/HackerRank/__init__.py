#!/usr/bin/env python
"""Add all of the modules in the current directory to __all__"""
import os
import sys

__all__ = []

for module in os.listdir(os.path.dirname(__file__)):
    if module != '__init__.py' and module[-3:] == '.py':
        __all__.append(module[:-3])


def get_modules(directory):
    """
    Load modules from files in a directory.
    For the api files and model files set the modname as the key
    and the class as the value.
    """
    modules = {}
    sys.path.append(directory)
    for filename in os.listdir(directory):
        if filename != '__init__.py' and filename.endswith(".py"):
            modname = filename[:-3]
            try:
                modules[modname] = getattr(__import__(modname), modname)
            except AttributeError:
                modules[modname] = __import__(modname)
    sys.path.pop()
    return modules


# load modules in the current directory and models directory.
# and update the globals package namespace.
current_dir = os.path.dirname(os.path.abspath(__file__))
globals().update(get_modules(current_dir))
globals().update(get_modules(os.path.join(current_dir, "models")))
