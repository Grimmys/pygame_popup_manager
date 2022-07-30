"""
Defines the initialization process of the package through the function init.
"""
from warnings import warn

from . import fonts

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

    fonts._init()
    _is_initialized = True
