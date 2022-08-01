"""
Defines the initialization process of the package through the function init.
"""
from warnings import warn

import pygame

from . import fonts
from ._exceptions.wrong_initialization_exception import WrongInitializationException

_is_initialized = False


def init() -> None:
    """
    Initialize the package modules.

    Must be called before all other calls and after the initialization of pygame.
    """
    global _is_initialized
    if _is_initialized:
        warn("pygamepopup is already initialized, no need to initialize it again")
        return

    if not pygame.get_init():
        raise WrongInitializationException(
            "pygamepopup.init() has to be called only after pygame.init()"
        )

    fonts._init()
    _is_initialized = True
