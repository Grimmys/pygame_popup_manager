"""
Defines the initialization process of the package through the function init.
"""

from . import fonts


def init() -> None:
    """
    Initialize the package modules.
    Must be called before all other calls and after the initialization of pygame.
    """
    fonts.init()
