import pygame
import pytest

import pygamepopup
from pygamepopup._exceptions.uninitialized_exception import UnintializedException
from pygamepopup.components import TextElement


def test_init_twice_prints_warning():
    pygame.init()
    pygamepopup.init()
    with pytest.warns(UserWarning):
        pygamepopup.init()


def test_use_anything_before_init_raises_uninitialized_exception():
    pygame.init()
    pygamepopup.initialization._is_initialized = False
    with pytest.raises(UnintializedException):
        TextElement("Try to create text element before init")