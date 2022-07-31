import pygame
import pytest

import src.pygamepopup as pygamepopup
from src.pygamepopup._exceptions.wrong_initialization_exception import WrongInitializationException
from src.pygamepopup.components import TextElement


def test_init_twice_prints_warning():
    pygame.init()
    pygamepopup.init()
    with pytest.warns(UserWarning):
        pygamepopup.init()


def test_use_anything_before_init_raises_wrong_initialization_exception():
    pygame.init()
    pygamepopup.initialization._is_initialized = False
    with pytest.raises(WrongInitializationException) as exception_info:
        TextElement("Try to create text element before init")
    assert exception_info.value.args[0] == "pygamepopup.init() has to be called before any other interaction with " \
                                           "pygamepopup"


def test_init_before_init_pygame_raises_wrong_initialization_exception():
    pygame.quit()
    with pytest.raises(WrongInitializationException) as exception_info:
        pygamepopup.init()
    assert "pygame.init()" in exception_info.value.args[0]
